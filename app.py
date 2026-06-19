import streamlit as st

st.set_page_config(
    page_title="Union Bank Fraud Analytics",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Union Bank Fraud Analytics Platform")

st.markdown("""
### Welcome

This platform includes:

- Executive Dashboard
- Fraud Prediction
- Fraud Analytics
- Product Analytics
- Model Insights

Use the sidebar to navigate between pages.
""")

st.success("Application Loaded Successfully")
