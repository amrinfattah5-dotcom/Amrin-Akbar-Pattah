from dask.distributed import Client
import dask.dataframe as dd
import dask
import pandas as pd
import os
import datetime
import glob

def main():

    # 1) Start Dask Client
    client = Client(n_workers=1, threads_per_worker=4, processes=True, memory_limit='2GB')
    print("Client started:", client)

    # 2) Create dataset
    df = dask.datasets.timeseries()
    print("\nDask DataFrame structure:")
    print(df)

    # 3) Buat folder data
    if not os.path.exists("data"):
        os.mkdir("data")

    # fungsi penamaan file
    def name(i):
        return str(datetime.date(2000, 1, 1) + i * datetime.timedelta(days=1))

    # 4) Save ke banyak file CSV
    print("\nWriting CSV files...")
    df.to_csv("data/*.csv", name_function=name)

    # 5) Cek file yang dibuat
    print("\nContoh file CSV (10 pertama):")
    files = sorted(glob.glob("data/*.csv"))
    for f in files[:10]:
        print(f)

    # 6) Baca salah satu file dengan pandas
    print("\nHead dari file CSV pertama:")
    pdf = pd.read_csv(files[0])
    print(pdf.head())

    # 7) Read semua CSV pakai Dask
    print("\nReading with dask.read_csv")
    ddf = dd.read_csv("data/2000-*.csv")
    print(ddf)

    # 8) Head ddf
    print("\nDask DataFrame head:")
    print(ddf.head())

    # 9) Write to Parquet
    print("\nWriting to Parquet...")
    ddf.to_parquet("parquet_data", engine="pyarrow", overwrite=True)

    # 10) Read Parquet
    print("\nReading Parquet:")
    parq = dd.read_parquet("parquet_data", engine="pyarrow")
    print(parq.head())

    print("\nSelesai!")
    client.close()


# WAJIB untuk Windows!!
if __name__ == "__main__":
    main()
