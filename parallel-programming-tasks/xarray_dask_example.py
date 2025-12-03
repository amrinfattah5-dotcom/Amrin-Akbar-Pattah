import dask.array as da
import xarray as xr
import numpy as np

def main():
    # Membuat data Dask Array besar
    data = da.random.random((5000, 5000), chunks=(1000, 1000))

    # Bungkus ke Xarray
    ds = xr.DataArray(data, dims=("x", "y"), name="contoh_data")

    print("Xarray + Dask Dataset:")
    print(ds)

    # Hitung mean
    result = ds.mean().compute()
    print("\nHasil mean:")
    print(result.values)

if __name__ == "__main__":
    main()
