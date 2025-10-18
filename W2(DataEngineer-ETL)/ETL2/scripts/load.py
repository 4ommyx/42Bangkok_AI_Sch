import os
import sqlite3
import pandas as pd

# .csv -> .db

def load():
    csv_path = "output/markets_summary.csv"
    db_path = "output/market.db"

    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)

    ####
    df.to_sql("user_sales_summary", conn, if_exists="replace", index=False)
    conn.close()
    print("\n✅ [LOAD] Data loaded into SQLite database successfully!")

load()