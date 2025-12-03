from dask.distributed import Client, as_completed
import time
import random

# fungsi: parse “file” — di contoh kita pakai nama file simulasi
def parse_file(fn: str):
    # simulasi waktu baca file
    time.sleep(random.random() * 0.5)
    # hasil parse: list nilai random sejumlah acak
    return [random.random() for _ in range(random.randint(1, 5))]

def process_item(x: float):
    # simulasi kerja berat kecil
    time.sleep(random.random() * 0.2)
    return x + 1

def main():
    client = Client(n_workers=4, threads_per_worker=1)
    print("Client:", client)

    filenames = [f"file_{i}.txt" for i in range(10)]

    # 1) Kirim parse_file ke semua file
    list_futures = client.map(parse_file, filenames, pure=False)

    # 2) Setelah parse selesai → ambil list hasil → submit process_item per elemen
    item_futures = []
    for future in as_completed(list_futures):
        lst = future.result()
        for x in lst:
            f2 = client.submit(process_item, x)
            item_futures.append(f2)

    # 3) Tunggu semua selesai & ambil hasil
    results = client.gather(item_futures)
    print("Results:", results)

if __name__ == "__main__":
    main()
