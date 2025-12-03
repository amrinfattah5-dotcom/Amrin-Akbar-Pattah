import os
import pandas as pd
import numpy as np

# Pastikan folder ada
os.makedirs("messy_data", exist_ok=True)

# 1. Buat 10 file CSV normal
for i in range(10):
    df = pd.DataFrame({
        "timestamp": pd.date_range("2000-01-01", periods=5),
        "name": ["Alice", "Bob", "Cindy", "Dave", "Eve"],
        "id": np.random.randint(900, 1100, size=5),
        "x": np.random.uniform(-1, 1, size=5),
        "y": np.random.uniform(-1, 1, size=5)
    })
    df.to_csv(f"messy_data/normal_{i}.csv", index=False)

# 2. Buat 1 file kosong (rusak)
open("messy_data/empty.csv", "w").close()

# 3. Buat 1 file dengan kolom hilang
df_missing = pd.DataFrame({
    "timestamp": pd.date_range("2000-01-01", periods=5),
    "name": ["Foo", "Bar", "Baz", "Qux", "Joe"],
    "id": np.random.randint(900, 1100, size=5),
    "x": np.random.uniform(-1, 1, size=5),
})
df_missing.to_csv("messy_data/missing_col.csv", index=False)

print("Selesai membuat messy data!")
