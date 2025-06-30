import streamlit as st

# Sidebar header
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("use the menu below to switch pages")

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💰 Personal Expense Tracker")
st.subheader("Track your expenses, analyze trends, and take control of your finances.")
st.markdown("""
This app helps you:
- Upload or manually add expense data
- Filter and visualize your spending
- Generate monthly summaries and trends

👈 Use the sidebar to navigate between pages.
""")

st.sidebar.image("https://icons.getbootstrap.com/icons/piggy-bank/", width=120)
st.sidebar.markdown("### 💼 Expense Tracker Pro")
st.sidebar.markdown("Track, analyze, and grow.")
