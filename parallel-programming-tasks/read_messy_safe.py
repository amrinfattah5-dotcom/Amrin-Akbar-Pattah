import os, glob
import pandas as pd
from dask import delayed
import dask.dataframe as dd

def safe_read(path):
    # jika file kosong → skip
    if os.path.getsize(path) == 0:
        print(f"Skip (empty): {path}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return pd.DataFrame()
    # pastikan kolom ada
    for col in ["timestamp", "name", "id", "x", "y"]:
        if col not in df.columns:
            df[col] = pd.NA
    return df

files = glob.glob("messy_data/*.csv")
print("Files:", files)

delayed_dfs = [delayed(safe_read)(f) for f in files]
dfs = [dd.from_delayed(d) for d in delayed_dfs]

df = dd.concat(dfs, axis=0, interleave_partitions=True)

print("=> head()")
print(df.head())

print("=> describe()")
print(df.describe().compute())
