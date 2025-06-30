import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

# Header
st.set_page_config(layout="wide")
st.title("📈 Expense Analysis Dashboard")
st.text("Changing budgeting one cell value at a time.")
st.divider()

# Load data
path = "data/expenses.csv"
if not os.path.exists(path):
    st.warning("No expenses data found. Please upload or add data first.")
    st.stop()

df = pd.read_csv(path)
st.write("Data Preview:")
st.dataframe(df.head())
st.divider()

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

# Filtering options
st.subheader("🔍 Filter")
filterable_columns = ['Category', 'Payment Method']
column = st.selectbox("Select column to filter by:", filterable_columns)

# Select value fron the column
unique_values = df[column].unique()
value = st.selectbox("Select value to filter by:", unique_values)

# Choose chart type
chart_type = st.selectbox("Select chart type:", ['Area', 'Bar', 'Line'])

# Button
if st.button("Generate Chart", type='primary'):
    # Filter the df
    filtered_df = df[df[column] == value]

    # Make sure date is in datetime format
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

    # Group by date and sum amounts
    chart_data = filtered_df.groupby('Date')['Amount'].sum().reset_index()

    # Sort by date
    chart_data = chart_data.sort_values('Date')

    # Show chart
    st.subheader(f"{chart_type} Chart for {value} in {column}")
    if chart_type == "Area":
        st.area_chart(chart_data.rename(columns={'Date': 'index'}).set_index('index'))
    elif chart_type == "Bar":
        st.bar_chart(chart_data.rename(columns={'Date': 'index'}).set_index('index'))
    elif chart_type == "Line":
        st.line_chart(chart_data.rename(columns={'Date': 'index'}).set_index('index'))
st.divider()

# Monthly Summary
st.subheader("📅 Monthly Summary by Category")
monthly_summary = df.groupby(['Month', 'Category'])['Amount'].sum().unstack().fillna(0)
st.dataframe(monthly_summary)
st.bar_chart(monthly_summary)
st.divider()

# Trends
st.subheader("📊 Spending Trends")
category_trend = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
st.bar_chart(category_trend)

monthly_trend = df.groupby(df['Date'].dt.to_period('M'))["Amount"].sum()
st.line_chart(monthly_trend)
