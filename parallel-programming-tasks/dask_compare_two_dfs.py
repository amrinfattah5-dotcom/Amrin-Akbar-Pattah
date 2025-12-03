from dask.distributed import Client
import pandas as pd
import dask.dataframe as dd

def main():
    client = Client(n_workers=1, threads_per_worker=4, processes=True, memory_limit='2GB')
    print("Client:", client)

    # --- DataFrame pertama menggunakan pandas ---
    df1 = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'nilai': [10, 20, 30, 40, 50],
        'kategori': ['A','A','B','B','C']
    })
    print("\nPandas DF1:")
    print(df1)

    # --- DataFrame kedua — juga pandas (atau bisa dask later) ---
    df2 = pd.DataFrame({
        'id': [3, 4, 5, 6, 7],
        'nilai': [300, 400, 500, 600, 700],
        'kategori': ['B','B','C','C','D']
    })
    print("\nPandas DF2:")
    print(df2)

    # --- Convert ke Dask DataFrame (opsional) ---
    ddf1 = dd.from_pandas(df1, npartitions=1)
    ddf2 = dd.from_pandas(df2, npartitions=1)
    print("\nDask DF1:", ddf1)
    print("Dask DF2:", ddf2)

    # --- Contoh compare: merge (inner) berdasarkan 'id' ---
    merged = ddf1.merge(ddf2, on='id', how='inner', suffixes=('_left','_right'))
    print("\nMerged DataFrames (inner join on id):")
    print(merged.compute())

    # --- Contoh concat (gabung baris dari kedua DF) ---
    concat = dd.concat([ddf1, ddf2], ignore_index=True)
    print("\nConcatenated (df1 + df2):")
    print(concat.compute())

    client.close()

if __name__ == "__main__":
    main()
