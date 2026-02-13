import os
import pandas as pd

# Resolve CSV path relative to this script's directory
data_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')

try:
    df = pd.read_csv(data_path)
    print("Data read successfully.")
except FileNotFoundError:
    print("Error: File not found. Ensure 'sales_data.csv' sits beside this script.")
    exit(1)

# Clean and prepare data types
df['sales'] = pd.to_numeric(df['sales'], errors='coerce').fillna(0)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Basic aggregates
total_sales = df['sales'].sum()
average_sales = df['sales'].mean()
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")

# Month filter (expects YYYY-MM like 2024-01)
month = input("Enter the year-month (YYYY-MM), e.g., 2024-01: ").strip()

if 'date' in df.columns and pd.api.types.is_datetime64_any_dtype(df['date']):
    filtered_df = df[df['date'].dt.strftime('%Y-%m') == month]
else:
    print("Warning: 'date' column is missing or not parseable; skipping month filter.")
    filtered_df = pd.DataFrame(columns=df.columns)

print(f"\nSales data for {month}:")
print(filtered_df if not filtered_df.empty else "No rows found for the selected month.")

# Sales by category
category_sales = df.groupby('category', dropna=False)['sales'].sum()
print("\nTotal Sales by Category:")
print(category_sales)