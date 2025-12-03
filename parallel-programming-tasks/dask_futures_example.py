from dask.distributed import Client
import random
import time

def inc(x):
    # simulasi tugas yang berat / lambat
    time.sleep(random.random())
    return x + 1

def double(x):
    time.sleep(random.random())
    return x * 2

def add(x, y):
    time.sleep(random.random())
    return x + y

def main():
    client = Client(n_workers=4)  # jalankan kluster lokal
    print("Client:", client)

    # Contoh: submit tugas satu per satu
    future1 = client.submit(inc, 1)
    future2 = client.submit(double, 2)

    # Chain / combinasikan futures
    future3 = client.submit(add, future1, future2)

    result = future3.result()  # tunggu hasil
    print("Hasil chain:", result)

    # Contoh: submit banyak tugas sekaligus dengan map
    inputs = list(range(10))
    futures = client.map(inc, inputs)

    # Tunggu semua selesai dan ambil hasil
    results = client.gather(futures)
    print("Hasil map inc:", results)

    # Contoh tugas bersarang / tree-like: misal naikkan semua bilangan 0–9 lalu jumlahkan
    doubled = client.map(double, inputs)
    total_future = client.submit(sum, doubled)
    print("Total after double:", total_future.result())

if __name__ == "__main__":
    main()
