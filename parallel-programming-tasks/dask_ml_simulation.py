from dask.distributed import Client
from dask import delayed
import numpy as np

def main():
    client = Client()
    print("Client:", client)

    X = np.random.random((100, 2))

    @delayed
    def train_chunk(chunk):
        print(f"Melatih chunk dengan {len(chunk)} data")
        return np.mean(chunk, axis=0)

    chunks = np.array_split(X, 4)
    results = [train_chunk(chunk) for chunk in chunks]

    final_result = delayed(np.mean)(results, axis=0)
    final = final_result.compute()

    print("Hasil akhir:", final)

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()
