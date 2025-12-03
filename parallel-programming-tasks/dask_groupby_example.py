from dask.distributed import Client
import dask
import dask.dataframe as dd

def main():
    # 1) Start Dask Client (opsional — untuk dashboard & performance)
    client = Client(n_workers=1, threads_per_worker=4, processes=True, memory_limit='2GB')
    print("Client started:", client)

    # 2) Buat dataset artificial timeseries sesuai di Dask example
    df = dask.datasets.timeseries()
    print("\nDask DataFrame structure:")
    print(df)

    # 3) Persist data ke memory (opsional — untuk performa jika dataset fit di RAM)
    df = df.persist()

    # 4) Contoh groupby: mean dari kolom 'x' berdasarkan kolom 'name'
    print("\n=== Groupby: mean(x) per name ===")
    res1 = df.groupby('name').x.mean().compute()
    print(res1)

    # 5) Contoh groupby + multiple aggregasi: mean & std pada 'x'; mean & count pada 'y'
    print("\n=== Groupby: multiple aggregations per name (x mean/std, y mean/count) ===")
    res2 = df.groupby('name').agg({
        'x': ['mean', 'std'],
        'y': ['mean', 'count']
    }).compute()
    print(res2)

    # Optionally — kalau mau: tampilkan beberapa baris hasil
    print("\n=== Sample hasil (5 teratas) ===")
    print(res2.head())

    client.close()
    print("\nDone.")

if __name__ == "__main__":
    main()
