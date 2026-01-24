import os
import pandas as pd

def analyze_sales_data(csv_file="sales_data.csv"):
    try:
        csv_path = os.path.join(os.path.dirname(__file__), csv_file)
        df = pd.read_csv(csv_path)

        print("\n CSV Loaded Successfully!\n")
        print(df.head())

        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")
        df = df.dropna(subset=["date", "product_category", "sales_amount"])

        total_sales = df["sales_amount"].sum()
        avg_sales = df["sales_amount"].mean()

        print("\n📌 Total Sales:", total_sales)
        print("📌 Average Sales:", round(avg_sales, 2))

        month_input = int(input("\nEnter month number (1-12): "))
        filtered_df = df[df["date"].dt.month == month_input]

        print(f"\n📌 Sales Data for Month {month_input}:")
        print(filtered_df.to_string(index=False) if not filtered_df.empty else "⚠️ No data found")

        category_sales = df.groupby("product_category")["sales_amount"].sum().reset_index()
        print("\n📌 Total Sales by Category:")
        print(category_sales.to_string(index=False))

    except FileNotFoundError:
        print("❌ sales_data.csv not found in exp-6 folder!")
    except Exception as e:
        print("❌ Something went wrong:", e)


if __name__ == "__main__":
    analyze_sales_data()   # no typing needed
