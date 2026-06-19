import streamlit as st

st.title("🧠 Model Insights")

st.metric(
    "Best Model",
    "XGBoost"
)

st.metric(
    "ROC-AUC",
    "0.99+"
)

st.markdown("---")

st.subheader("Confusion Matrix Results")

st.markdown("""
True Negatives : 18501

False Positives : 60

False Negatives : 251

True Positives : 1188
""")

st.markdown("---")

st.subheader("Business Recommendations")

st.info("""
1. Monitor high-value transactions.

2. Add additional verification for international transactions.

3. Apply stricter fraud rules during risky time periods.

4. Use risk-based authentication.

5. Continuously retrain the model using recent transaction data.
""")

st.markdown("---")

st.subheader("Top Fraud Drivers")

st.success("""
• Foreign Transaction

• Amount Log

• Merchant Group

• Card Entry Method

• Time Bin

• Country of Transaction
""")

st.markdown("---")

st.subheader("Model Deployment Decision")

st.write("""
Low Risk → Approve

Medium Risk → OTP Verification

High Risk → Block Transaction
""")
