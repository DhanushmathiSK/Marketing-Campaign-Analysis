
import pandas as pd
import numpy as np

# Load the original dataset
df = pd.read_csv("../dataset/marketing_campaign_data.csv")

print("Original dataset shape:", df.shape)

# Remove duplicate records
df = df.drop_duplicates()

# Convert customer registration date into datetime format
df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    errors="coerce",
    dayfirst=True
)

# Check missing values in Income
print("\nMissing Income values before cleaning:")
print(df["Income"].isnull().sum())

# Replace missing Income values with the median
df["Income"] = df["Income"].fillna(df["Income"].median())

# Create Age column
current_year = 2026
df["Age"] = current_year - df["Year_Birth"]

# Create Total Spend column
spending_columns = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds"
]

df["Total_Spend"] = df[spending_columns].sum(axis=1)

# Create Total Purchases column
purchase_columns = [
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases"
]

df["Total_Purchases"] = df[purchase_columns].sum(axis=1)

# Create Children column
df["Children"] = df["Kidhome"] + df["Teenhome"]

# Display cleaned dataset
print("\nCleaned dataset shape:", df.shape)

print("\nNew columns:")
print(df[["Age", "Total_Spend", "Total_Purchases", "Children"]].head())

# Save cleaned dataset
df.to_csv("../dataset/marketing_campaign_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
