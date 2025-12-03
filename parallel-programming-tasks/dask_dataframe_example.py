import dask.dataframe as dd
from dask.distributed import Client
import pandas as pd

def main():
    client = Client()
    print(client)

    # Buat DataFrame contoh
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona", "George", "Hannah", "Ian", "Jane"],
        "year": [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022, 2022],
        "month": [1,1,2,1,3,2,1,2,3,3],
        "day": [1,2,3,4,5,6,7,8,9,10],
        "score": [85, 92, 78, 88, 95, 70, 60, 99, 82, 91]
    }
    df = pd.DataFrame(data)

    # Konversi ke Dask DataFrame
    ddf = dd.from_pandas(df, npartitions=2)

    # Tampilkan dataframe asli
    print("\n=== DATAFRAME ASLI ===")
    print(ddf.compute())

    # Tambah kolom score kuadrat
    ddf["score_squared"] = ddf["score"] ** 2
    print("\n=== SCORE KUADRAT ===")
    print(ddf.compute())

    # Filter score > 90
    high_score = ddf[ddf["score"] > 90]
    print("\n=== SCORE > 90 ===")
    print(high_score.compute())

    # Tambah kolom score + 5
    ddf["score_plus5"] = ddf["score"] + 5
    print("\n=== SCORE + 5 ===")
    print(ddf.compute())

    # Tambah kolom score * 2
    ddf["score_times2"] = ddf["score"] * 2
    print("\n=== SCORE TIMES 2 ===")
    print(ddf.compute())

    # Group by year, hitung total score tiap tahun
    grouped = ddf.groupby("year")["score"].sum().compute()
    print("\n=== TOTAL SCORE PER YEAR ===")
    print(grouped)

if __name__ == "__main__":
    main()
