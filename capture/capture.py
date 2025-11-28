from scapy.all import sniff, IP, TCP, UDP, get_if_list
import time
from threading import Lock

flows = {}
flows_lock = Lock()

def process_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        sport = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else 0
        dport = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else 0
        key = (src, dst, sport, dport, proto)
        with flows_lock:
            if key not in flows:
                flows[key] = {"pkts": 0, "bytes": 0, "start": time.time()}
            flows[key]["pkts"] += 1
            flows[key]["bytes"] += len(packet)

def start_capture(interface):
    sniff(iface=interface, prn=process_packet, store=False)

def auto_interface():
    interfaces = get_if_list()
    if len(interfaces) == 1:
        return interfaces[0]
    return interfaces[1]
