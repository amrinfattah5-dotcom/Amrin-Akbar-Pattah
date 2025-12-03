import dask.array as da
import numpy as np
import numba
from dask.distributed import Client

# Stencil manual (tanpa gufunc)
@numba.njit
def smooth_block(x):
    out = np.empty_like(x)
    for i in range(1, x.shape[0] - 1):
        for j in range(1, x.shape[1] - 1):
            out[i, j] = (
                x[i-1, j-1] + x[i-1, j] + x[i-1, j+1] +
                x[i,   j-1] + x[i,   j] + x[i,   j+1] +
                x[i+1, j-1] + x[i+1, j] + x[i+1, j+1]
            ) // 9
    return out

def main():
    client = Client()
    print(client)

    # array 2D saja -> lebih stabil
    x = da.random.randint(0, 255, size=(2000, 2000), chunks=(500, 500), dtype=np.int32)

    # pakai map_blocks (aman untuk Dask HLG)
    y = x.map_blocks(smooth_block, dtype=np.int32)

    result = y.compute()
    print("DONE. shape =", result.shape)
    print(result[:5, :5])

if __name__ == "__main__":
    main()
