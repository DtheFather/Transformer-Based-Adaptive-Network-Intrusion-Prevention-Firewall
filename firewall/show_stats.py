import os
import csv
from collections import Counter
from tabulate import tabulate

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "results", "firewall_log.csv")

if not os.path.exists(LOG_PATH):
    print("No log file found. Run defender or block_ip first.")
    raise SystemExit()

rows = []
with open(LOG_PATH, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

ip_counts = Counter(r["ip"] for r in rows)
table = [[ip, count] for ip, count in ip_counts.most_common()]

print("\nBlocked IP summary:\n")
print(tabulate(table, headers=["IP", "Times Blocked"]))

print("\nLast 5 events:\n")
for r in rows[-5:]:
    print(f'{r["timestamp_utc"]}  {r["ip"]}  score={r["score"]}')
