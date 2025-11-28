import subprocess
import os
import csv
import datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "results", "firewall_log.csv")

def ensure_logfile():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp_utc", "ip", "score"])

def block_ip(ip, score=None):
    ensure_logfile()
    cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]
    subprocess.run(cmd)

    ts = datetime.datetime.utcnow().isoformat()
    score_val = "" if score is None else float(score)

    with open(LOG_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, ip, score_val])

    print(f"[DEFENDER] Blocked {ip} at {ts} score={score_val}")
