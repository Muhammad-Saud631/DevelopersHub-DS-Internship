import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("📊 Global Superstore Business Dashboard")

# Load Dataset
df = pd.read_csv("business-dashboard/Global_Superstore.csv", encoding='latin1')

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')

# Sidebar Filters
st.sidebar.header("Filter Options")

region = st.sidebar.selectbox("Select Region", df['Region'].unique())
category = st.sidebar.selectbox("Select Category", df['Category'].unique())

# Filter Data
filtered_df = df[(df['Region'] == region) & (df['Category'] == category)]

# KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

st.metric("💰 Total Sales", f"${total_sales:,.2f}")
st.metric("📈 Total Profit", f"${total_profit:,.2f}")

# Top 5 Customers
st.subheader("🏆 Top 5 Customers by Sales")

top_customers = (
    filtered_df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

st.bar_chart(top_customers)

# Sales Trend
st.subheader("📅 Sales Trend Over Time")

sales_trend = (
    filtered_df.groupby('Order Date')['Sales']
    .sum()
)

st.line_chart(sales_trend)
