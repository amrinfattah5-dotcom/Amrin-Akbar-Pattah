import pandas as pd
import numpy as np
from dask import delayed
import dask.dataframe as dd
import glob

# 1 — definisikan fungsi untuk baca file CSV dengan proteksi
def read_data(filename):
    # schema / tipe kolom yang kita harapkan
    dtype = {'id': int, 'name': str, 'x': float, 'y': float}

    try:
        df = pd.read_csv(filename, dtype=dtype)
    except Exception as e:
        # kalau gagal (file korup / kosong / rusak), buat DataFrame kosong dg kolom sesuai schema
        df = pd.DataFrame({col: pd.Series(dtype=typ) for col, typ in dtype.items()})

    # jika kolom ‘y’ hilang — tambahkan dengan NaN
    if 'y' not in df.columns:
        df['y'] = np.NaN

    return df

# 2 — cari semua file data (misalnya di folder data/)
files = glob.glob('data/*.csv')

# 3 — lakukan delayed read untuk tiap file
dfs = [delayed(read_data)(f) for f in files]

# 4 — gabungkan semua delayed pandas DataFrame jadi Dask DataFrame
ddf = dd.from_delayed(dfs)

print("Dask DataFrame (lazy):")
print(ddf)

print("\nBeberapa data awal:")
print(ddf.head())  # trigger pembacaan

print("\nStatistik deskriptif (full compute):")
print(ddf.describe().compute())
