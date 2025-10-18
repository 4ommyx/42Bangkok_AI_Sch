import pandas as pd
import os

def transform():
    staged_dir = "data/staged"

    # --- Load cleaned CSVs ---
    products = pd.read_csv(os.path.join(staged_dir, "products_clean.csv"))
    transactions = pd.read_csv(os.path.join(staged_dir, "transactions_clean.csv"))
    users = pd.read_csv(os.path.join(staged_dir, "users_clean.csv"))
    
    # Join
    merged = transactions.merge(users, on="user_id").merge(products, on="product_id")

    # Aggregate
    summary = merged.groupby(["user_id", "name", "city"]).agg(
        total_spent = ("amount", "sum"),
        avg_spent = ("amount", "mean"),
        transactions_count = ("transaction_id", "count"),
        unique_categories = ("category", pd.Series.nunique)
    ).reset_index()

    os.makedirs("output", exist_ok=True)
    summary.to_csv(os.path.join("output/user_sales_summary.csv"), index=False)
    print("\n✅ [TRANSFORM] User sales summary saved successfully!")

transform()
