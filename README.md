# Marketing Campaign Analysis

## Project Overview

This project analyses customer purchasing behaviour and marketing campaign performance using Python, SQL and Streamlit.

The objective is to identify valuable customer segments, understand campaign response patterns, analyse product preferences and provide data-driven marketing recommendations.

## Business Objectives

- Analyse customer demographics and purchasing behaviour.
- Evaluate marketing campaign acceptance and response rates.
- Identify high-value customers and potential non-responders.
- Understand purchasing patterns across different channels.
- Identify customer segments for targeted marketing.
- Present business insights through an interactive dashboard.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| MySQL | Database management and SQL analysis |
| Streamlit | Interactive dashboard |
| Matplotlib / Seaborn | Data visualisation |

## Dataset Overview

- Total records: 56,000 customers
- Total columns: 28
- Each row represents a customer.

Key information includes:
- Customer demographics: Age, Education, Marital Status and Income.
- Product spending: Wines, Fruits, Meat, Fish, Sweets and Gold.
- Purchasing channels: Web, Catalogue and Store.
- Campaign history: AcceptedCmp1 to AcceptedCmp5.
- Campaign response: Response.

## Project Workflow

### 1. Data Understanding
- Examined dataset dimensions and column information.
- Reviewed data types and statistical summaries.

### 2. Data Quality Assessment
- Checked missing values.
- Examined duplicate records.
- Reviewed data consistency.

### 3. Data Cleaning
- Prepared customer data for analysis.
- Created additional analytical columns.

### 4. Feature Engineering
Created derived metrics:
- Age
- Total_Spend
- Total_Purchases
- Children

### 5. SQL Database Setup
- Created the marketing campaign database.
- Loaded customer records.
- Performed SQL-based analytical queries.

### 6. Exploratory Data Analysis
Analysed:
- Campaign response rates.
- Product category spending.
- Income-wise spending.
- Age-wise spending.
- Marital-status-wise spending.
- Purchase channel preferences.
- Website visits and web purchases.
- High-value customer segments.

### 7. Interactive Dashboard
Developed a Streamlit dashboard to present customer and campaign insights.

## Key Business Insights

### Overall Campaign Performance
- Total customers analysed: 56,000.
- Customers who responded: 8,265.
- Overall response rate: 14.76%.

### Campaign Performance
- Campaign 1 recorded the highest acceptance rate: 13.44%.
- Campaign 2 recorded the lowest acceptance rate: 1.44%.

### Product Preferences
- Meat Products recorded the highest total spending.
- Wines ranked second.
- Fruits recorded the lowest total spending.

### Purchase Channel Analysis
- Store purchases: 263,559.
- Web purchases: 237,938.
- Catalogue purchases: 118,202.

Physical stores recorded the highest purchase volume, followed by web purchases.

### Customer Segmentation
Customers with income above 75K recorded a 23.54% response rate, the highest among the income groups analysed.

Very high spenders recorded a 29.63% response rate.

The combined segment of customers with income above 75K and spending of at least 2,000 recorded a 31.31% response rate.

### High-Value Customer Analysis
Within the above-75K income and very-high-spending segment:

- Customers aged 40–49 recorded the highest response rate: 32.93%.
- Customers aged 60 and above contributed the highest number of responders: 271.

## Business Recommendations

1. Prioritise high-income and high-spending customers for targeted campaign testing.
2. Develop personalised campaigns for valuable customers who have not responded.
3. Investigate opportunities to improve website purchase conversion.
4. Maintain the strong physical-store channel while improving digital engagement.
5. Evaluate campaign performance using response rate, conversion value and campaign cost.

## Project Structure

```text
Marketing-Campaign-Analysis/
│
├── dataset/
│   ├── marketing_campaign_data.csv
│   ├── marketing_data_dictionary.csv
│   ├── marketing_campaign_cleaned.csv
│   └── marketing_campaign_segmented.csv
│
├── python_scripts/
│   ├── 01_dataset_understanding.py
│   ├── 02_data_quality_check.py
│   ├── 03_data_cleaning.py
│   ├── 04_feature_engineering.py
│   └── 05_sql_database_setup.py
│
├── mc.py
└── README.md
```

## Skills Demonstrated

- Data Cleaning and Data Quality Assessment
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Python and Pandas
- SQL Queries and Aggregations
- Customer Segmentation
- Business Analysis
- Data Visualisation
- Interactive Dashboard Development

## Conclusion

This project demonstrates an end-to-end marketing campaign analysis workflow, from raw customer data preparation to SQL-based business analysis and interactive dashboard development.

The analysis highlights customer segments with stronger campaign responses and identifies opportunities to improve customer engagement and marketing targeting.

## Author

Dhanushmathi S K

GitHub: https://github.com/DhanushmathiSK
