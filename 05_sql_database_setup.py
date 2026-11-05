import sqlite3
import pandas as pd
import os

print("--- Step 5: Setting up SQLite Database & Running Analytics ---")

# 1. Load the segmented dataset (adjust path if running from root vs python_scripts folder)
# Assuming you are running from the root 'Marketing_Campaign_Analysis' folder:
data_path = "dataset/marketing_campaign_segmented.csv"
df = pd.read_csv(data_path)

# 2. Create the sql folder if it doesn't exist
os.makedirs("sql", exist_ok=True)
db_path = "sql/marketing_analytics.db"

# 3. Connect to SQLite database (creates the file automatically)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 4. Load the dataframe into a SQLite table named 'customers'
df.to_sql("customers", conn, if_exists="replace", index=False)
print(f"Successfully loaded {len(df)} rows into SQLite database table: 'customers'")

# 5. Write and execute an analytical SQL query to check campaign response rates by Marital Status
query_marital_response = """
SELECT 
    Marital_Status,
    COUNT(ID) AS Total_Customers,
    ROUND(AVG(Income), 2) AS Average_Income,
    ROUND(AVG(Total_Spend), 2) AS Average_Spend,
    ROUND(AVG(Segment_Campaign_Responder) * 100, 2) AS Response_Rate_Percent
FROM customers
GROUP BY Marital_Status
ORDER BY Average_Spend DESC;
"""

result_df = pd.read_sql_query(query_marital_response, conn)
print("\n--- SQL Query Results: Campaign Response & Spend by Marital Status ---")
print(result_df)

# Close connection
conn.close()
print("\nDatabase setup and query execution completed successfully!")