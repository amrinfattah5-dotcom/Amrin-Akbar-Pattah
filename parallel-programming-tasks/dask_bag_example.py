from dask.distributed import Client
import dask.bag as db

def main():
    # 1. Jalankan Dask Client
    client = Client(n_workers=2, threads_per_worker=1)
    print(client)

    # 2. Buat Bag dari list Python
    b = db.from_sequence([1,2,3,4,5,6,7,8], npartitions=2)
    print("Asli:", b.compute())

    # 3. Map (ubah setiap elemen)
    squared = b.map(lambda x: x*x)
    print("Kuadrat:", squared.compute())

    # 4. Filter (ambil genap)
    evens = b.filter(lambda x: x % 2 == 0)
    print("Genap:", evens.compute())

    # 5. Kombinasi map + filter
    result = b.filter(lambda x: x % 2 == 1).map(lambda x: x*10)
    print("Filter odd + x10:", result.compute())

if __name__ == "__main__":
    main()
