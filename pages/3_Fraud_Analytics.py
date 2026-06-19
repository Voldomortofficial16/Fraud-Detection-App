import streamlit as st
import pandas as pd

df = pd.read_csv("fraud_data.csv")

st.title("📈 Fraud Analytics")

st.subheader("Fraud by Merchant Group")

merchant = (
    df.groupby("Merchant Group")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(merchant)

st.subheader("Fraud by Country")

country = (
    df.groupby("Country of Transaction")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(country)

st.subheader("Fraud by Card Type")

card = (
    df.groupby("Type of Card")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(card)

st.subheader("Fraud by Time Bin")

time = (
    df.groupby("Time_Bin")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(time)

st.subheader("Fraud by Bank")

bank = (
    df.groupby("Bank")["Fraud"]
      .mean()
      .sort_values(ascending=False)
)

st.bar_chart(bank)
