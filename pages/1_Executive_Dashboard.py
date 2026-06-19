import streamlit as st
import pandas as pd

df = pd.read_csv("fraud_data.csv")

st.title("📊 Executive Dashboard")

# KPIs
col1, col2, col3, col4 = st.columns(4)

total_txn = len(df)
fraud_txn = df["Fraud"].sum()
fraud_rate = round((fraud_txn / total_txn) * 100, 2)
avg_amount = round(df["Amount"].mean(), 2)

col1.metric(
    "Total Transactions",
    f"{total_txn:,}"
)

col2.metric(
    "Fraud Transactions",
    f"{fraud_txn:,}"
)

col3.metric(
    "Fraud Rate",
    f"{fraud_rate}%"
)

col4.metric(
    "Avg Amount",
    f"₹{avg_amount}"
)

st.markdown("---")

# Business Impact
st.subheader("💰 Estimated Business Impact")

estimated_loss = fraud_txn * avg_amount

st.metric(
    "Potential Fraud Exposure",
    f"₹{estimated_loss:,.0f}"
)

st.markdown("---")

# Fraud Distribution
st.subheader("📈 Fraud vs Non-Fraud")

fraud_dist = df["Fraud"].value_counts()

st.bar_chart(fraud_dist)

st.markdown("---")

# Top Merchant Risk
st.subheader("🏪 Fraud Rate by Merchant Group")

merchant_risk = (
    df.groupby("Merchant Group")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(merchant_risk)

st.markdown("---")

# Country Risk
st.subheader("🌍 Fraud Rate by Country")

country_risk = (
    df.groupby("Country of Transaction")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(country_risk)

st.markdown("---")

# Business Recommendations

st.subheader("🎯 Executive Recommendations")

st.info("""
• High-risk merchant groups should undergo enhanced monitoring.

• International transactions require stronger verification.

• Fraud prevention can significantly reduce financial exposure.

• Risk-based authentication should be applied to high-value transactions.
""")
