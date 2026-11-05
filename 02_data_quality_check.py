
import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("../dataset/marketing_campaign_data.csv")
# 2. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 3. Check total missing values
print("\nTotal missing values:")
print(df.isnull().sum().sum())

# 4. Check duplicate records
print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# 5. Check duplicate customer IDs
print("\n--- DUPLICATE CUSTOMER IDs ---")
print(df["ID"].duplicated().sum())

# 6. Check column data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 7. Statistical summary of numerical columns
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())

# 8. Check unique values in categorical columns
print("\n--- CATEGORICAL VALUES ---")
print("Education:", df["Education"].unique())
print("Marital Status:", df["Marital_Status"].unique())
print("Countries:", df["Country"].unique())
