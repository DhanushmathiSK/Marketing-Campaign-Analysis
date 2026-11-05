
import pandas as pd

# Step 1: Load marketing dataset
df = pd.read_csv("../dataset/marketing_campaign_data.csv")

# Step 2: Display first 5 records
print("FIRST 5 RECORDS")
print(df.head())

# Step 3: Check number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# Step 4: Check column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Step 5: Check data types and missing values
print("\nDATASET INFORMATION")
df.info()
