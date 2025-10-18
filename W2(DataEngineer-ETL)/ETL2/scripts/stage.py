import pandas as pd
import numpy as np
import os

def stage():
    staged_dir = "data/staged"

    # Your code load a df
    market_df = pd.read_csv(os.path.join(staged_dir, "market.csv"))

    # Fill missing numerical column with median
    num_cols = market_df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        median_value = market_df[col].median()
        market_df[col].fillna(median_value, inplace=True)

    # Fill missing categorical column with mode
    cat_cols = market_df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        mode_value = market_df[col].mode()[0]
        market_df[col].fillna(mode_value, inplace=True)


    # Optional: Add row id
    market_df.reset_index(drop=True, inplace=True)
    market_df.index.name = 'row_id'
    market_df.index = market_df.index + 1

    market_df.to_csv(os.path.join(staged_dir, "market_clean.csv"), index=False)

    print("successfully staged market.csv")
   
stage()


