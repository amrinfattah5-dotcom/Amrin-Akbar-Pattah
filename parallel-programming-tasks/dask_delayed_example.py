# dask_delayed_example.py
from dask import delayed, compute
from dask.distributed import Client
import time

@delayed
def inc(x):
    # contoh pekerjaan berat: tidur 1 detik dulu
    time.sleep(1)
    return x + 1

@delayed
def double(x):
    time.sleep(1)
    return x * 2

@delayed
def add(x, y):
    return x + y

def main():
    client = Client()
    print("Client:", client)

    data = [1, 2, 3, 4, 5]

    results = []
    for x in data:
        a = inc(x)
        b = double(x)
        c = add(a, b)
        results.append(c)

    # total: jumlah semua hasil
    total = delayed(sum)(results)

    # compute sekaligus semua
    final = total.compute()
    print("Hasil akhir:", final)

if __name__ == "__main__":
    main()
