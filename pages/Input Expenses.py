import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("📂 Upload & Add Expenses")

path = "data/expenses.csv"
os.makedirs("data", exist_ok=True)

# Load data
if os.path.exists(path):
    df = pd.read_csv(path)
else:
    df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Payment Method'])

# CSV upload
st.subheader("📤 Upload CSV")
uploaded_file = st.file_uploader("Upload a CSV file with matching columns", type="csv")
if uploaded_file:
    uploaded_df = pd.read_csv(uploaded_file)
    df = pd.concat([df, uploaded_df], ignore_index=True)
    df.to_csv(path, index=False)
    st.success("✅ File uploaded and merged!")

# Manual input
st.subheader("➕ Manually Add an Expense")
with st.form("manual_form"):
    date = st.date_input("Date", datetime.today())
    category = st.selectbox("Category", ["Food", "Rent", "Travel", "Utilities", "Entertainment", "Health", "Shopping", "Education", "Other"])
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, step=0.1)
    method = st.selectbox("Payment Method", ['Cash', 'M-Pesa', 'Debit Card', 'Credit Card', 'Bank Transfer'])
    submitted = st.form_submit_button("Add Expense", type='primary')

if submitted:
    new_row = {
        "Date": pd.to_datetime(date).strftime('%Y-%m-%d'),
        "Category": category,
        "Description": description,
        "Amount": amount,
        "Payment Method": method
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(path, index=False)
    st.success("✅ Expense added!")

# Preview data
if not df.empty:
    st.subheader("📋 Current Expenses")
    st.dataframe(df.tail(5))