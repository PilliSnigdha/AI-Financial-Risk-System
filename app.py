import streamlit as st
import plotly.express as px

from models.analysis import load_data
from models.forecast import forecast_expense
from models.risk_model import calculate_risk
from models.anomaly import detect_anomalies

st.title("AI Financial Risk & Spending Intelligence System")

# Load data
df = load_data("data/finance_data.csv")

# Detect anomalies
df = detect_anomalies(df)

st.subheader("Financial Data")
st.write(df)

# Expense trend chart
fig = px.line(df, x="Month", y="Total_Expense", title="Monthly Expense Trend")
st.plotly_chart(fig)

# Forecast
prediction = forecast_expense(df)
st.subheader(f"Predicted Next Month Expense: ₹{prediction}")

# Risk calculation
latest_ratio = df["Savings_Ratio"].iloc[-1]
risk = calculate_risk(latest_ratio)

st.subheader(f"Financial Risk Level: {risk}")

if risk == "High":
    st.error("High Financial Risk - Reduce expenses")
elif risk == "Medium":
    st.warning("Moderate Risk - Monitor spending")
else:
    st.success("Low Risk - Good financial health")

# Show anomalies
st.subheader("Anomaly Detection")
st.write(df[df["Anomaly"] == -1])