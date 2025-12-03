import dask.dataframe as dd
import glob
from dask.delayed import delayed
import pandas as pd
import os

# 1. cari file csv
files = glob.glob('messy_data/*.csv')
print("Files ditemukan:", files)

if not files:
    raise FileNotFoundError("Tidak ada file dalam folder messy_data/*.csv")

# 2. Reader dengan pengecekan file kosong
def my_reader(path):
    if os.path.getsize(path) == 0:
        print(f"Skip file kosong: {path}")
        return pd.DataFrame()   # kembalikan dataframe kosong
    return pd.read_csv(path)

# 3. Load semua file pakai delayed
dfs = [dd.from_delayed(delayed(my_reader)(path)) for path in files]

# 4. gabungkan dataframe (skip dataframe kosong)
df = dd.concat(dfs, interleave_partitions=True)

# 5. Tampilkan head
print("\n=== Beberapa data awal ===")
print(df.head())

# 6. Statistik
print("\n=== Statistik deskriptif ===")
print(df.describe().compute())
