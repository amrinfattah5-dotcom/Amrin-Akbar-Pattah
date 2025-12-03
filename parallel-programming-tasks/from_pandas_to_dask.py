import pandas as pd
import dask.dataframe as dd

# --- Bagian 1: From Pandas to Dask ---
pdf = pd.DataFrame({
    'x': range(10),
    'y': range(10, 20)
})

ddf = dd.from_pandas(pdf, npartitions=3)

print("=== Dask DataFrame ===")
print(ddf)

print("\n=== Compute hasil ===")
print(ddf.compute())


# --- Bagian 2: GOTCHA's from Pandas to Dask ---

# Contoh .loc assignment tidak didukung
try:
    ddf.loc[0, 'x'] = 999
except Exception as e:
    print("\nGOTCHA 1: .loc assignment tidak didukung di Dask:")
    print(e)

# Contoh inplace=True tidak didukung
try:
    ddf.rename(columns={'x': 'x_new'}, inplace=True)
except Exception as e:
    print("\nGOTCHA 2: inplace=True tidak didukung di Dask:")
    print(e)

# Cara benar rename di Dask
ddf2 = ddf.rename(columns={'x': 'x_new'})
print("\nRename yang benar:")
print(ddf2.compute())


# --- Bagian 3: apply dengan meta ---
def tambah_satu(v):
    return v + 1

ddf3 = ddf['y'].apply(tambah_satu, meta=('y', 'int64'))
print("\nApply dengan meta:")
print(ddf3.compute())
