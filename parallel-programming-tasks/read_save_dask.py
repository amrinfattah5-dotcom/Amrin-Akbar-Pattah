import dask.dataframe as dd

# --- 3a. Read (baca) banyak file CSV sekaligus ---
# gunakan glob pattern supaya Dask baca semua CSV yang cocok
ddf = dd.read_csv('file*.csv')  

print("=== Dask DataFrame (lazy) ===")
print(ddf)

print("\n=== Beberapa baris awal (head) ===")
print(ddf.head())

print("\n=== Compute dan tampil seluruh DF ===")
print(ddf.compute())

# --- 3b. Simpan (save) ke file CSV via Dask ---
# misalnya kita simpan ke folder 'output'
ddf.to_csv('output/result-*.csv', index=False)

print("\nSelesai: Dask DataFrame disimpan ke file CSV di folder 'output'")
