# dask_image_example.py
import os
from skimage import data, io
import dask_image.imread
import dask_image.ndfilters
import numpy as np
import matplotlib.pyplot as plt

def prepare_image():
    # pakai gambar astronaut dari skimage sample
    img = data.astronaut()
    os.makedirs("img_temp", exist_ok=True)
    path = os.path.join("img_temp", "astronaut.png")
    io.imsave(path, img)
    return path

def main():
    path = prepare_image()
    print("Image saved to:", path)

    # 1) Load image ke dask array
    arr = dask_image.imread.imread(path)
    print("Dask image array:", arr)

    # 2) Convert ke grayscale (custom function)
    def grayscale(rgb):
        return (rgb[..., 0]*0.2125 + rgb[..., 1]*0.7154 + rgb[..., 2]*0.0721).astype(np.uint8)

    gray = grayscale(arr[0])  # arr[0] is the single frame
    result = gray.compute()  # compute the chunk
    print("Result shape:", result.shape)

    # 3) Tampilkan hasil
    fig, (ax0, ax1) = plt.subplots(1, 2)
    ax0.imshow(arr[0])
    ax0.set_title("Original")
    ax1.imshow(result, cmap="gray")
    ax1.set_title("Grayscale")
    plt.show()

if __name__ == "__main__":
    main()
