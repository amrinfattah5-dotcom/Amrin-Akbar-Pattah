import asyncio
from time import sleep
from dask.distributed import Client, LocalCluster


async def async_work(x):
    print(f"[ASYNC] start {x}")
    await asyncio.sleep(1)
    return x * 10


def run_async_inside_worker(x):
    """Worker menjalankan async function secara lokal."""
    return asyncio.run(async_work(x))


async def main():
    print("Membuat Dask cluster...")
    cluster = LocalCluster(n_workers=2, threads_per_worker=1)
    client = Client(cluster)

    print("Mengirim task ke Dask...")
    futures = []

    for i in range(5):
        f = client.submit(run_async_inside_worker, i)
        futures.append(f)

    print("Mengumpulkan hasil...")
    results = client.gather(futures)

    print("\nHASIL:")
    for r in results:
        print(r)

    print("\nSelesai!")


if __name__ == "__main__":
    asyncio.run(main())
