import pandas as pd
import os

def stage():
    staged_dir = "data/staged"

    # --- Load CSVs ---
    products = pd.read_csv(os.path.join(staged_dir, "products.csv"))
    transactions = pd.read_csv(os.path.join(staged_dir, "transactions.csv"))
    users = pd.read_csv(os.path.join(staged_dir, "users.csv"))

    # --- Display info ---
    for name, df in [("products", products), ("transactions", transactions), ("users", users)]:
        print(f"[STAGE] {name}: {df.shape[0]} rows, {df.shape[1]} columns")

    # --- Convert datetime columns ---
    # Assuming transaction_date and birthdate are Unix timestamps (milliseconds)
    transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"], unit="ms", errors="coerce")
    users["birthdate"] = pd.to_datetime(users["birthdate"], unit="ms", errors="coerce")

    # --- Drop duplicates ---
    transactions = transactions.drop_duplicates(subset=["transaction_id"])
    users = users.drop_duplicates(subset=["user_id"])
    products = products.drop_duplicates(subset=["product_id"])

    # --- Save cleaned files ---
    products.to_csv(os.path.join(staged_dir, "products_clean.csv"), index=False)
    transactions.to_csv(os.path.join(staged_dir, "transactions_clean.csv"), index=False)
    users.to_csv(os.path.join(staged_dir, "users_clean.csv"), index=False)

    print("\n✅ [STAGE] Cleaned CSVs saved successfully!")

stage()