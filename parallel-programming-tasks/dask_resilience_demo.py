from dask.distributed import Client

def safe_div(a, b):
    return a / b

def normal_task(x):
    return x * x

def main():
    client = Client(n_workers=2, threads_per_worker=1)
    print("Dashboard:", client.dashboard_link)

    # ----- Tugas normal -----
    futures1 = client.map(normal_task, list(range(5)))

    # ----- Tugas error (division by zero) -----
    future_error = client.submit(safe_div, 1, 0)

    # ----- Tugas lanjutan yang tergantung hasil error -----
    # Ini akan error juga karena future_error gagal
    future_dependent = client.submit(normal_task, future_error)

    # ----- Print semua hasil -----
    all_futures = futures1 + [future_error, future_dependent]

    for f in all_futures:
        try:
            result = f.result()
            print("Result:", result)
        except Exception as e:
            print("Task failed:", repr(e))

    client.shutdown()

if __name__ == "__main__":
    main()
