import os
import sys
import time
import csv
import torch
import torch.nn as nn

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from capture.capture import flows, flows_lock
from firewall.blocker import block_ip

model_path = os.path.join(os.path.dirname(__file__), "..", "model", "tranwall.pt")
model_path = os.path.abspath(model_path)

checkpoint = torch.load(model_path, map_location="cpu", weights_only=False)
scaler_mean = torch.tensor(checkpoint["scaler_mean"], dtype=torch.float32)
scaler_scale = torch.tensor(checkpoint["scaler_scale"], dtype=torch.float32)
input_dim = int(checkpoint["input_dim"])
state = checkpoint["model_state_dict"]

FLOWS_SNAPSHOT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "results", "flows_snapshot.csv")
)

class TranWallNet(nn.Module):
    def __init__(self, input_dim, d_model=64, nhead=8, num_layers=2, dim_feedforward=128, dropout=0.1):
        super().__init__()
        self.input_proj = nn.Linear(input_dim, d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.cls_head = nn.Sequential(
            nn.Linear(d_model, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.input_proj(x)
        x = x.unsqueeze(1)
        x = self.transformer(x)
        x = x[:, 0, :]
        logits = self.cls_head(x)
        return logits.squeeze(1)

model = TranWallNet(input_dim=input_dim)
model.load_state_dict(state)
model.eval()

def flow_to_features(flow_dict):
    vec = torch.zeros(input_dim, dtype=torch.float32)
    pkts = float(flow_dict["pkts"])
    byt = float(flow_dict["bytes"])
    dur = float(time.time() - flow_dict["start"])
    vec[0] = pkts
    vec[1] = byt
    vec[2] = dur
    vec = (vec - scaler_mean) / scaler_scale
    return vec

def write_flows_snapshot():
    os.makedirs(os.path.dirname(FLOWS_SNAPSHOT_PATH), exist_ok=True)
    with flows_lock:
        items = list(flows.items())
    now = time.time()
    with open(FLOWS_SNAPSHOT_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["src_ip", "dst_ip", "sport", "dport", "proto", "pkts", "bytes", "duration_sec"])
        for (src, dst, sport, dport, proto), data in items:
            dur = now - data["start"]
            writer.writerow([src, dst, sport, dport, proto, data["pkts"], data["bytes"], f"{dur:.2f}"])

def monitor(threshold=0.9, sleep_sec=2.0):
    print("[DEFENDER] started, monitoring flows")
    while True:
        with flows_lock:
            items = list(flows.items())
        total_flows = len(items)
        blocked = 0
        for key, f in items:
            src_ip = key[0]
            x = flow_to_features(f).unsqueeze(0)
            with torch.no_grad():
                prob = torch.sigmoid(model(x)).item()
            if prob >= threshold:
                block_ip(src_ip, prob)
                with flows_lock:
                    if key in flows:
                        del flows[key]
                blocked += 1

        write_flows_snapshot()
        print(f"[DEFENDER] flows={total_flows} blocked_this_round={blocked}")
        time.sleep(sleep_sec)
