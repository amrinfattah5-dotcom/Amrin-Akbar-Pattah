from dask.distributed import Client, LocalCluster
from prophet import Prophet
import pandas as pd
import numpy as np

# ----------------------------------------------------------
# Buat data otomatis
# ----------------------------------------------------------
def generate_fake_data():
    np.random.seed(0)
    dates = pd.date_range(start="2020-01-01", periods=200)
    
    df = pd.DataFrame({
        "series_id": ["A"] * 200 + ["B"] * 200,
        "ds": list(dates) + list(dates),
        "y": np.random.randn(200).cumsum().tolist()
             + (np.random.randn(200).cumsum() + 50).tolist()
    })
    return df

# ----------------------------------------------------------
# Fungsi forecasting Prophet
# ----------------------------------------------------------
def forecast_one_group(df):
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    forecast["series_id"] = df["series_id"].iloc[0]
    return forecast[["series_id", "ds", "yhat"]]

# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------
def main():
    print("Membuat cluster Dask...")
    cluster = LocalCluster()
    client = Client(cluster)
    print("Dask Client:", client)

    print("Membuat dataset otomatis...")
    df_all = generate_fake_data()

    print("Memecah dataset per series_id...")
    groups = [group for _, group in df_all.groupby("series_id")]

    print("Submit job Prophet ke Dask...")
    futures = [client.submit(forecast_one_group, g) for g in groups]

    print("Mengumpulkan hasil...")
    results = client.gather(futures)

    print("\n=== HASIL FORECAST ===")
    final = pd.concat(results)
    print(final.head())
    print("\nSelesai! Semua forecasting berhasil.")

if __name__ == "__main__":
    main()
