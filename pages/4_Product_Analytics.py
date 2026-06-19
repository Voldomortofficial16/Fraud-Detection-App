import streamlit as st
import pandas as pd

df = pd.read_csv("fraud_data.csv")

st.title("📱 Product Analytics")

st.subheader("Transaction Type Distribution")

txn = (
    df["Type of Transaction"]
      .value_counts()
)

st.bar_chart(txn)

st.subheader("Age Group Distribution")

age = (
    df["Age Group"]
      .value_counts()
)

st.bar_chart(age)

st.subheader("Bank Usage")

bank = (
    df["Bank"]
      .value_counts()
)

st.bar_chart(bank)

st.subheader("Gender Distribution")

gender = (
    df["Gender"]
      .value_counts()
)

st.bar_chart(gender)

st.subheader("Country Distribution")

country = (
    df["Country of Residence"]
      .value_counts()
)

st.bar_chart(country)

st.subheader("Business Insights")

st.success("""
• Younger users prefer digital channels.

• Some banks show significantly higher transaction volume.

• Customer segmentation helps design targeted banking products.

• Country-wise transaction behaviour helps identify growth opportunities.
""")
