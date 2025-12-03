from dask.distributed import Client
import dask.dataframe as dd
import pandas as pd
import dask
import numpy as np

def main():
    # Start client (opsional tapi berguna jika dataset besar / paralel)
    client = Client(n_workers=1, threads_per_worker=4, processes=True, memory_limit='2GB')
    print("Client started:", client)

    # --- 1) buat data Pandas (contoh kecil) ---
    data = {
        'A': np.random.rand(1000),
        'B': np.random.randint(0, 100, size=1000),
        'C': np.random.choice(['X','Y','Z'], size=1000)
    }
    pdf = pd.DataFrame(data)
    print("\nPandas DataFrame head:")
    print(pdf.head())

    # --- 2) Convert ke Dask DataFrame ---
    ddf = dd.from_pandas(pdf, npartitions=10)
    print("\nConverted to Dask DataFrame:")
    print(ddf)

    # --- 3) Contoh operasi lazy (filter + groupby) ---
    print("\n--- Operasi Dask (lazy) ---")
    ddf2 = ddf[ddf['A'] > 0.5]  # filter
    ddf_group = ddf2.groupby('C').B.mean()  # groupby + aggregate → masih lazy
    print("Dask object (lazy):", ddf_group)

    # --- 4) Compute hasilnya agar menjadi Pandas Series/DataFrame ---
    result = ddf_group.compute()
    print("\nHasil compute (mean B per C):")
    print(result)

    client.close()

if __name__ == "__main__":
    main()
