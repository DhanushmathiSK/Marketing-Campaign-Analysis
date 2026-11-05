import pandas as pd
import numpy as np

print("--- Step 4: Starting Feature Engineering & Segmentation ---")

# 1. Load the cleaned dataset from the dataset folder
file_path = "dataset/marketing_campaign_cleaned.csv"
df = pd.read_csv(file_path)

# 2. Derive Customer Age (using 2026 as reference year)
current_year = 2026
df['Age'] = current_year - df['Year_Birth']

# 3. Calculate Total Spend across all product categories
df['Total_Spend'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 
                        'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

# 4. Calculate Total Purchases across channels
df['Total_Purchases'] = df[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)

# 5. Calculate Total Children
df['Children'] = df['Kidhome'] + df['Teenhome']

# 6. Customer Tenure Calculation
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
reference_date = pd.to_datetime('2014-12-31')
df['Customer_Tenure_Months'] = ((reference_date - df['Dt_Customer']).dt.days / 30).astype(int)

print("Derived metrics created successfully!")

# --- Rule-Based Segmentation ---
# 90th percentile threshold for high spenders
high_spend_threshold = df['Total_Spend'].quantile(0.90)

df['Segment_High_Income'] = np.where(df['Income'] > 75000, 1, 0)
df['Segment_Young_Customer'] = np.where(df['Age'] < 30, 1, 0)
df['Segment_Campaign_Responder'] = np.where(df['Response'] == 1, 1, 0)
df['Segment_High_Web_Engagement'] = np.where(df['NumWebVisitsMonth'] > 5, 1, 0)
df['Segment_Family_Customer'] = np.where(df['Children'] > 0, 1, 0)
df['Segment_High_Spender'] = np.where(df['Total_Spend'] > high_spend_threshold, 1, 0)

# 7. Save the fully segmented data back to your dataset folder
output_path = "dataset/marketing_campaign_segmented.csv"
df.to_csv(output_path, index=False)

print(f"Success! Saved segmented data to: {output_path}")