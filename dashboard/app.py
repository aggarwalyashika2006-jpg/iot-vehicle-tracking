import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Vehicle Tracking Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 IoT Vehicle Tracking & Theft Prevention Dashboard")

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "location_log.csv"
)

if not os.path.exists(csv_path):
    st.error("No location data found.")
    st.stop()

df = pd.read_csv(csv_path)

if len(df) == 0:
    st.warning("CSV file is empty.")
    st.stop()

latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latitude",
        latest["Latitude"]
    )

with col2:
    st.metric(
        "Longitude",
        latest["Longitude"]
    )

with col3:
    st.metric(
        "Distance (km)",
        latest["Distance(km)"]
    )

with col4:
    st.metric(
        "Status",
        latest["Status"]
    )

st.markdown("---")

if latest["Alert"] == "NONE":
    st.success("✅ Vehicle Safe")
else:
    st.error("🚨 Theft Alert Detected")

st.markdown("---")

st.subheader("📍 Live Vehicle Location")

map_df = pd.DataFrame({
    "lat": [latest["Latitude"]],
    "lon": [latest["Longitude"]]
})

st.map(map_df)

st.markdown("---")

st.subheader("📄 Recent Records")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

st.markdown("---")

st.subheader("📈 Distance Trend")

st.line_chart(
    df["Distance(km)"]
)

st.subheader("📈 Latitude Trend")

st.line_chart(
    df["Latitude"]
)

st.subheader("📈 Longitude Trend")

st.line_chart(
    df["Longitude"]
)

st.markdown("---")

st.subheader("📊 Statistics")

colA, colB, colC = st.columns(3)

with colA:
    st.info(
        f"Total Records: {len(df)}"
    )

with colB:
    st.warning(
        f"Theft Alerts: {len(df[df['Status'] == 'THEFT SUSPECTED'])}"
    )

with colC:
    st.success(
        f"Safe Records: {len(df[df['Status'] == 'MOVING SAFELY'])}"
    )