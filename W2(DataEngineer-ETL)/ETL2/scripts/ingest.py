import os
import shutil


def ingest():
    src_dir = r"data\raw"
    dest_dir = r"data\staged"
    os.makedirs(dest_dir, exist_ok=True)

    for filename in ["market.csv"]:
        shutil.copy(os.path.join(src_dir, filename), os.path.join(dest_dir, filename))
        print("successfully ingested", filename)

ingest()