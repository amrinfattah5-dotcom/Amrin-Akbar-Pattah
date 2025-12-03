import requests
import pandas as pd
import dask.dataframe as dd

if __name__ == "__main__":
    # 1. Ambil data JSON dari web (tanpa Dask)
    url = "https://jsonplaceholder.typicode.com/posts"
    data = requests.get(url).json()

    # 2. Convert ke Pandas
    pdf = pd.DataFrame(data)

    # 3. Convert ke Dask DataFrame
    ddf = dd.from_pandas(pdf, npartitions=4)

    print(ddf.head())
    print("\nTotal rows:", ddf.shape[0].compute())
