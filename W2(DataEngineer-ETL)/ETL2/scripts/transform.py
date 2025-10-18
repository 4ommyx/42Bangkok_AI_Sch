import pandas as pd
import numpy as np
import os

def transform():
    staged_dir = "data/staged"
    #  Your code load a df
    market_df = pd.read_csv(os.path.join(staged_dir, "market_clean.csv"))

    # transform data stock to boolean
    market_df['Stock_status'] = market_df['Stock'].apply(lambda x: 1 if x == 'In Stock' else 0)


    # Aggregate by category
    category_summary = market_df.groupby('Category').agg(
        total_sales=('Price', 'sum'),
        average_price=('Price', 'mean'),
        transaction_count=('Category', 'count'),
        rating_avg=('Rating', 'mean'),
        discount_avg=('Discount', 'mean'),
        stock_percentage=("Stock_status", 'mean')
    ).reset_index()

    # Save category summary
    os.makedirs("output", exist_ok=True)
    category_summary.to_csv(os.path.join("output/markets_summary.csv"), index=False)
    print("\n✅ [TRANSFORM] Markets summary saved successfully!")

transform()