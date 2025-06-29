import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Header
st.title("Personal Expense Tracker Dashboard")
st.text("Changing budgeting one cell value at a time.")

# Load data
df = pd.read_csv("data/expenses.csv")
st.write("Data Preview:")
st.dataframe(df.head())

# Filtering options
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

