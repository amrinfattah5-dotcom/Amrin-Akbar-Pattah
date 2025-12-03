from dask import delayed, compute
from dask.distributed import Client, LocalCluster
import random
import time

def costly_simulation(params):
    # simulate pekerjaan berat
    time.sleep(random.random())  # delay acak 0-1 detik
    return sum(params)

if __name__ == "__main__":
    # setup cluster lokal
    cluster = LocalCluster(n_workers=4, threads_per_worker=1)
    client = Client(cluster)
    print("Cluster:", client)

    # buat list parameter input
    inputs = [
        [random.random() for _ in range(10)]
        for _ in range(100)  # 100 simulasi
    ]

    # gunakan dask.delayed
    tasks = [delayed(costly_simulation)(inp) for inp in inputs]

    # jalankan paralel
    results = compute(*tasks)

    print("Results:", results[:5])
    print("Finished", len(results), "simulations")
