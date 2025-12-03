import pandas as pd
import dask.dataframe as dd
import os

# === FUNGSI PEMBACA CSV AMAN ===
def load_csv_safe(path):
    try:
        df = pd.read_csv(path)

        # Tambah kolom yang hilang
        for col in ["timestamp", "name", "id", "x", "y"]:
            if col not in df.columns:
                df[col] = pd.NA

        # Samakan tipe
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df["name"] = df["name"].astype("object")
        df["id"] = pd.to_numeric(df["id"], errors="coerce")
        df["x"] = pd.to_numeric(df["x"], errors="coerce")
        df["y"] = pd.to_numeric(df["y"], errors="coerce")

        return df

    except Exception as e:
        print(f"Skip {path}: {e}")
        return None

# === LOAD SEMUA FILE ===
folder = "messy_data"
all_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".csv")]
print("Semua file:", all_files)

dfs = []
for path in all_files:
    df = load_csv_safe(path)
    if df is not None:
        dfs.append(df)
        print(f"Loaded: {path} shape={df.shape}")

if not dfs:
    print("Tidak ada file valid.")
    exit()

# === META (hanya untuk concat) ===
meta = dfs[0].head(0)

# === BUAT DASK DF (tanpa meta) ===
dasked = [dd.from_pandas(df, npartitions=1) for df in dfs]

# === CONCAT DENGAN META ===
ddf = dd.concat(dasked, axis=0, interleave_partitions=True, meta=meta)

# === OUTPUT ===
print("\n=== HEAD ===")
print(ddf.head())

print("\n=== DESCRIBE ===")
print(ddf.describe().compute())
