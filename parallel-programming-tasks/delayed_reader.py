import os
import pandas as pd
import dask
import dask.dataframe as dd
from dask.delayed import delayed

folder = "messy_data"

files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".csv")]
print("Files ditemukan:", files)

# Schema yang benar sesuai data normal
meta = pd.DataFrame({
    "timestamp": pd.Series(dtype="object"),
    "name": pd.Series(dtype="object"),
    "id": pd.Series(dtype="int64"),
    "x": pd.Series(dtype="float64"),
    "y": pd.Series(dtype="float64"),
})

@delayed
def load_file(path):
    # Tangkap file kosong tanpa header
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        print(f"Skip file kosong (no header): {path}")
        return meta.copy()

    # Kalau file ada header tapi isinya kosong
    if df.empty:
        print(f"Skip file kosong: {path}")
        return meta.copy()

    # Lengkapi kolom jika ada yang hilang
    for col in meta.columns:
        if col not in df.columns:
            df[col] = None

    # Samakan tipe data sesuai meta
    df = df.astype(meta.dtypes.to_dict())

    return df[meta.columns]

# Convert ke Dask DataFrame
delayed_dfs = [load_file(f) for f in files]
df = dd.from_delayed(delayed_dfs, meta=meta)

print("\n=== HEAD ===")
print(df.head())

print("\n=== DESCRIBE ===")
print(df.describe().compute())
