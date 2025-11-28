import os
import sys
import threading
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from capture.capture import start_capture, auto_interface
from firewall.defender import monitor

def main():
    if hasattr(os, "geteuid"):
        if os.geteuid() != 0:
            print("Run this script with sudo so that packet capture and iptables work")
            sys.exit(1)
    iface = auto_interface()
    print(f"[APP] using interface {iface}")
    t = threading.Thread(target=start_capture, args=(iface,), daemon=True)
    t.start()
    print("[APP] capture started, starting defender")
    time.sleep(1.0)
    monitor()

if __name__ == "__main__":
    main()
