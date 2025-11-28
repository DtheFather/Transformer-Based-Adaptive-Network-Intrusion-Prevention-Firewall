import os
from pathlib import Path
import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT_DIR / "results" / "firewall_log.csv"
FLOWS_PATH = ROOT_DIR / "results" / "flows_snapshot.csv"

st.set_page_config(page_title="TranWall Firewall Dashboard", layout="wide")

st.title("🛡️ TranWall – Firewall Dashboard")

if not LOG_PATH.exists():
    st.warning(f"No log file found at {LOG_PATH}. Run the firewall first so it can log blocks.")
    st.stop()

@st.cache_data(ttl=5.0)
def load_log():
    df = pd.read_csv(LOG_PATH)
    if df.empty:
        return df
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], errors="coerce")
    df = df.dropna(subset=["timestamp_utc"])
    return df

df = load_log()

if df.empty:
    st.info("Log file exists but no blocks have been recorded yet.")
else:
    total_blocks = len(df)
    unique_ips = df["ip"].nunique()
    avg_score = pd.to_numeric(df["score"], errors="coerce").mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total blocks", total_blocks)
    col2.metric("Unique IPs blocked", unique_ips)
    col3.metric("Average score", f"{avg_score:.3f}" if pd.notna(avg_score) else "N/A")

    st.markdown("---")

    st.subheader("📊 Blocks per IP")
    blocks_per_ip = df["ip"].value_counts().reset_index()
    blocks_per_ip.columns = ["ip", "count"]
    if not blocks_per_ip.empty:
        st.bar_chart(blocks_per_ip.set_index("ip"))
    else:
        st.write("No IPs blocked yet.")

    st.subheader("📈 Blocks over time")
    df_time = df.sort_values("timestamp_utc")
    df_time_indexed = df_time.set_index("timestamp_utc")
    blocks_per_min = df_time_indexed.resample("1min").size()
    blocks_per_min.name = "blocks"

    if not blocks_per_min.empty:
        st.line_chart(blocks_per_min)
    else:
        st.write("No time data available for plotting.")

    st.subheader("🧾 Last 20 block events")
    st.dataframe(
        df.sort_values("timestamp_utc", ascending=False).head(20),
        use_container_width=True
    )

st.markdown("---")
st.subheader("📡 Live flows snapshot")

@st.cache_data(ttl=2.0)
def load_flows():
    if not FLOWS_PATH.exists():
        return pd.DataFrame()
    flows_df = pd.read_csv(FLOWS_PATH)
    return flows_df

flows_df = load_flows()

if flows_df.empty:
    st.info("No flow snapshot yet. Make sure the backend (tranwall_cli.py) is running and some traffic is hitting the interface.")
else:
    st.dataframe(
        flows_df.sort_values("pkts", ascending=False).head(50),
        use_container_width=True
    )

if st.button("Refresh data"):
    st.cache_data.clear()
    st.experimental_rerun()
