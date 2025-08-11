import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==== Page Config ====
st.set_page_config(page_title="Weather Dashboard", layout="wide")

# ==== Title ====
st.title("How's the weather? 🌤️")

# ==== File Path ====
file_path = r"D:\Deep Learning\weather_forecast_data.csv"

if not os.path.exists(file_path):
    st.error(f"File not found at: {file_path}")
else:
    df = pd.read_csv(file_path)

    # Show raw data
    if st.checkbox("Show raw data"):
        st.write(df)

    # ==== Current Weather ====
    latest_row = df.iloc[-1]  # last row
    st.subheader("Current Weather 🌡️")

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature (°C)", latest_row["Temperature"])
    col2.metric("Humidity (%)", latest_row["Humidity"])
    col3.metric("Pressure (hPa)", latest_row["Pressure"])

    col4, col5, col6 = st.columns(3)
    col4.metric("Wind Speed (m/s)", latest_row["Wind_Speed"])
    col5.metric("Cloud Cover (%)", latest_row["Cloud_Cover"])
    col6.metric("Rain (mm)", latest_row["Rain"])

    # ==== Week Ahead Graph ====
    st.subheader("Week Ahead 📅")
    st.caption("Temperature and rainfall forecast")

    fig, ax1 = plt.subplots(figsize=(10, 5))

    days = [f"Day {i+1}" for i in range(len(df))]

    # Temperature line
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Temperature °C", color="tab:red")
    ax1.plot(days, df["Temperature"], color="tab:red", marker="o", label="Temperature °C")
    ax1.tick_params(axis="y", labelcolor="tab:red")
    plt.xticks(rotation=45)

    # Rainfall bars
    ax2 = ax1.twinx()
    ax2.set_ylabel("Rain (mm)", color="tab:blue")
    ax2.bar(days, df["Rain"], color="tab:blue", alpha=0.3, label="Rain (mm)")
    ax2.tick_params(axis="y", labelcolor="tab:blue")

    fig.tight_layout()
    st.pyplot(fig)

