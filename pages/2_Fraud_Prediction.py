import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("🤖 Fraud Prediction")

model = joblib.load("fraud_model.pkl")
encoder = joblib.load("encoder.pkl")

day = st.selectbox(
    "Day of Week",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
)

card = st.selectbox(
    "Type of Card",
    ["Visa","MasterCard"]
)

entry = st.selectbox(
    "Entry Mode",
    ["PIN","Tap","CVC"]
)

amount = st.number_input(
    "Amount",
    min_value=1.0,
    value=100.0
)

txn_type = st.selectbox(
    "Type of Transaction",
    ["ATM","POS","Online"]
)

merchant = st.selectbox(
    "Merchant Group",
    ["Electronics","Food","Restaurant","Services","Entertainment"]
)

country_txn = st.selectbox(
    "Country of Transaction",
    ["USA","United Kingdom","India","China"]
)

shipping = st.selectbox(
    "Shipping Address",
    ["USA","United Kingdom","India","China"]
)

country_res = st.selectbox(
    "Country of Residence",
    ["USA","United Kingdom","India","China"]
)

gender = st.selectbox(
    "Gender",
    ["M","F"]
)

age = st.slider(
    "Age",
    18,
    80,
    35
)

bank = st.selectbox(
    "Bank",
    ["HSBC","Barclays","Lloyds","Monzo","RBS"]
)

if st.button("Predict Fraud"):

    amount_log = np.log1p(amount)

    foreign_transaction = int(
        country_txn != country_res
    )

    high_amount = int(
        amount > 200
    )

    if age <= 25:
        age_group = "18-25"
    elif age <= 35:
        age_group = "26-35"
    elif age <= 45:
        age_group = "36-45"
    elif age <= 55:
        age_group = "46-55"
    elif age <= 65:
        age_group = "56-65"
    else:
        age_group = "65+"

    current_hour = 20

    if current_hour < 6:
        time_bin = "Night"
    elif current_hour < 12:
        time_bin = "Morning"
    elif current_hour < 18:
        time_bin = "Afternoon"
    else:
        time_bin = "Evening"

    card_entry = f"{card}_{entry}"

    input_df = pd.DataFrame({

        "Day of Week":[day],
        "Type of Card":[card],
        "Entry Mode":[entry],
        "Amount":[amount],
        "Type of Transaction":[txn_type],
        "Merchant Group":[merchant],
        "Country of Transaction":[country_txn],
        "Shipping Address":[shipping],
        "Country of Residence":[country_res],
        "Gender":[gender],
        "Age":[age],
        "Bank":[bank],
        "Age Group":[age_group],
        "Foreign_Transaction":[foreign_transaction],
        "Amount_Log":[amount_log],
        "Time_Bin":[time_bin],
        "Card_Entry":[card_entry],
        "High_Amount":[high_amount]

    })

    encoded = encoder.transform(input_df)

    prob = model.predict_proba(encoded)[0][1]

    st.metric(
        "Fraud Probability",
        f"{prob:.2%}"
    )

    if prob < 0.30:
        st.success("✅ Low Risk → Approve")

    elif prob < 0.70:
        st.warning("⚠ Medium Risk → OTP Verification")

    else:
        st.error("🚨 High Risk → Block Transaction")
