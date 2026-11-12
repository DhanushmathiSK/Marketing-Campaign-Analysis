
import pandas as pd
import pymysql

# MySQL connection details
host = "localhost"
user = "root"
password = "mathi@2K"
database = "marketing_campaign_db"

# Connect to MySQL server
connection = pymysql.connect(
    host=host,
    user=user,
    password=password
)

cursor = connection.cursor()

# Create database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print("Database created or already exists!")

# Select database
cursor.execute(f"USE {database}")

# Load segmented CSV
df = pd.read_csv("../dataset/marketing_campaign_segmented.csv")

# Create table automatically using CSV column names
columns = []

for column in df.columns:
    columns.append(f"`{column}` TEXT")

create_table_query = f"""
CREATE TABLE IF NOT EXISTS customers (
    {', '.join(columns)}
)
"""

cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute(create_table_query)

print("Customers table created!")

# Insert records in batches
column_names = [f"`{col}`" for col in df.columns]
placeholders = ", ".join(["%s"] * len(df.columns))

insert_query = f"""
INSERT INTO customers ({', '.join(column_names)})
VALUES ({placeholders})
"""

data = [
    tuple(None if pd.isna(value) else str(value) for value in row)
    for row in df.itertuples(index=False, name=None)
]

batch_size = 1000

for start in range(0, len(data), batch_size):
    batch = data[start:start + batch_size]
    cursor.executemany(insert_query, batch)
    connection.commit()

print("Customer data successfully loaded!")
print("Total records loaded:", len(data))

# Verify record count
cursor.execute("SELECT COUNT(*) FROM customers")
print("Records in MySQL:", cursor.fetchone()[0])

cursor.close()
connection.close()

print("MySQL connection closed successfully!")
