import streamlit as st

st.set_page_config(
    page_title="Union Bank Fraud Analytics",
    layout="wide"
)

st.title("🏦 Union Bank Fraud Analytics Platform")

st.markdown("""
### Features

- Fraud Prediction
- Executive Dashboard
- Fraud Analytics
- Product Analytics
- SHAP Explainability
- Risk Segmentation

Use the sidebar to navigate.
""")
import streamlit as st
import pandas as pd

df = pd.read_csv("fraud_data.csv")

st.title("📊 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    len(df)
)

col2.metric(
    "Fraud Transactions",
    df["Fraud"].sum()
)

col3.metric(
    "Fraud Rate %",
    round(
        df["Fraud"].mean()*100,
        2
    )
)

col4.metric(
    "Avg Amount",
    round(
        df["Amount"].mean(),
        2
    )
)

st.subheader("Potential Savings")

tp = 1188
loss_per_fraud = 5000

savings = tp * loss_per_fraud

st.metric(
    "Estimated Savings",
    f"₹{savings:,.0f}"
)
import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load(
    "fraud_model.pkl"
)

encoder = joblib.load(
    "encoder.pkl"
)

st.title("🤖 Fraud Prediction")

day = st.selectbox(
    "Day of Week",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
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
    min_value=0.0
)

txn_type = st.selectbox(
    "Transaction Type",
    ["ATM","POS","Online"]
)

merchant = st.text_input(
    "Merchant Group"
)

country_txn = st.text_input(
    "Country of Transaction"
)

shipping = st.text_input(
    "Shipping Address"
)

country_res = st.text_input(
    "Country of Residence"
)

gender = st.selectbox(
    "Gender",
    ["M","F"]
)

age = st.number_input(
    "Age",
    min_value=18.0,
    max_value=100.0
)

bank = st.text_input(
    "Bank"
)

if st.button("Predict"):

    amount_log = np.log1p(amount)

    foreign_txn = int(
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

    time_bin = "Evening"

    card_entry = (
        card + "_" + entry
    )

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
        "Foreign_Transaction":[foreign_txn],
        "Amount_Log":[amount_log],
        "Time_Bin":[time_bin],
        "Card_Entry":[card_entry],
        "High_Amount":[high_amount]

    })

    encoded = encoder.transform(
        input_df
    )

    prob = model.predict_proba(
        encoded
    )[0][1]

    st.metric(
        "Fraud Probability",
        f"{prob:.2%}"
    )

    if prob < 0.3:
        st.success(
            "Low Risk"
        )

    elif prob < 0.7:
        st.warning(
            "Medium Risk"
        )

    else:
        st.error(
            "High Risk"
        )
      import streamlit as st
import pandas as pd

df = pd.read_csv(
    "fraud_data.csv"
)

st.title("📈 Fraud Analytics")

st.subheader(
    "Fraud by Merchant"
)

merchant = (
    df.groupby(
        "Merchant Group"
    )["Fraud"]
    .mean()
)

st.bar_chart(
    merchant
)

st.subheader(
    "Fraud by Country"
)

country = (
    df.groupby(
        "Country of Transaction"
    )["Fraud"]
    .mean()
)

st.bar_chart(
    country
)

st.subheader(
    "Fraud by Time"
)

time = (
    df.groupby(
        "Time_Bin"
    )["Fraud"]
    .mean()
)

st.bar_chart(
    time
)
import streamlit as st
import pandas as pd

df = pd.read_csv(
    "fraud_data.csv"
)

st.title(
    "📱 Product Analytics"
)

st.subheader(
    "Transaction Type Usage"
)

txn = (
    df["Type of Transaction"]
    .value_counts()
)

st.bar_chart(
    txn
)

st.subheader(
    "Age Group Usage"
)

age = (
    df["Age Group"]
    .value_counts()
)

st.bar_chart(
    age
)

st.subheader(
    "Bank Usage"
)

bank = (
    df["Bank"]
    .value_counts()
)

st.bar_chart(
    bank
)
import streamlit as st

st.title(
    "🧠 Model Insights"
)

st.markdown("""
### Best Model

XGBoost

### ROC-AUC

0.99+

### Business Insights

- Foreign transactions are high risk
- High Amount transactions increase fraud probability
- Certain Merchant Groups exhibit elevated fraud rates
- Night transactions show higher fraud activity
- Risk segmentation enables targeted verification

### Deployment Decision

Low Risk → Approve

Medium Risk → OTP Verification

High Risk → Block Transaction
""")
