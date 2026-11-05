import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Marketing Campaign Dashboard", layout="wide")

# Helper function to query the SQLite database
def load_data_from_sql(query):
    # Adjust path to point from 'dashboard/' folder to 'sql/' folder
    db_path = "sql/marketing_analytics.db"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.title("📊 Marketing Campaign Analytics & Customer Segmentation")
st.markdown("Interactive dashboard designed for management to evaluate campaign performance and customer behaviors.")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")

# Get list of countries for filtering
try:
    countries_df = load_data_from_sql("SELECT DISTINCT Country FROM customers")
    country_list = countries_df['Country'].tolist()
except Exception as e:
    st.error("Could not load database. Make sure Step 5 (SQL setup) has been run successfully!")
    st.stop()

selected_country = st.sidebar.multiselect("Select Country", options=country_list, default=country_list)

# Format for SQL IN clause
if not selected_country:
    country_filter = "('All')"
else:
    country_filter = "('" + "', '".join(selected_country) + "')"

# --- TOP-LEVEL KPI METRICS ---
kpi_query = f"""
SELECT 
    COUNT(ID) as total_customers, 
    AVG(Total_Spend) as avg_spend, 
    AVG(Segment_Campaign_Responder) * 100 as response_rate 
FROM customers 
WHERE Country IN {country_filter}
"""
kpi_data = load_data_from_sql(kpi_query)

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{kpi_data['total_customers'].values[0]:,}")
col2.metric("Average Customer Spend", f"${kpi_data['avg_spend'].values[0]:,.2f}")
col3.metric("Campaign Response Rate", f"{kpi_data['response_rate'].values[0]:.2f}%")

st.markdown("---")

# --- SECTION 1: PRODUCT SPENDING BREAKDOWN ---
st.subheader("🛍️ Average Spending Across Product Categories")

spend_query = f"""
SELECT 
    AVG(MntWines) as Wine, 
    AVG(MntFruits) as Fruits, 
    AVG(MntMeatProducts) as Meat, 
    AVG(MntFishProducts) as Fish, 
    AVG(MntSweetProducts) as Sweets, 
    AVG(MntGoldProds) as Gold 
FROM customers 
WHERE Country IN {country_filter}
"""
spend_df = load_data_from_sql(spend_query).melt(var_name="Product", value_name="Average Spend")

fig, ax = plt.subplots(figsize=(10, 4))
sns.barplot(data=spend_df, x="Product", y="Average Spend", ax=ax, palette="Blues_d")
plt.title("Average Spend per Product Category")
plt.xticks(rotation=0)
st.pyplot(fig)

# --- SECTION 2: SEGMENT RESPONSE RATES ---
st.subheader("🎯 Campaign Response Rate by Customer Segment")

segment_query = f"""
SELECT 'High Income' as Segment, AVG(Segment_Campaign_Responder)*100 as Conversion FROM customers WHERE Segment_High_Income = 1 AND Country IN {country_filter}
UNION
SELECT 'Young Customer', AVG(Segment_Campaign_Responder)*100 FROM customers WHERE Segment_Young_Customer = 1 AND Country IN {country_filter}
UNION
SELECT 'High Web Engagement', AVG(Segment_Campaign_Responder)*100 FROM customers WHERE Segment_High_Web_Engagement = 1 AND Country IN {country_filter}
UNION
SELECT 'Family Customer', AVG(Segment_Campaign_Responder)*100 FROM customers WHERE Segment_Family_Customer = 1 AND Country IN {country_filter}
UNION
SELECT 'High Spender', AVG(Segment_Campaign_Responder)*100 FROM customers WHERE Segment_High_Spender = 1 AND Country IN {country_filter}
"""
seg_df = load_data_from_sql(segment_query)

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(data=seg_df, x="Segment", y="Conversion", ax=ax2, palette="Greens_r")
plt.title("Conversion Rate (%) by Behavioral Segment")
plt.xticks(rotation=15)
st.pyplot(fig2)