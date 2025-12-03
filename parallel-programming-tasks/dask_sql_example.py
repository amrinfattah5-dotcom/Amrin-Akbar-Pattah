# file: test_dasksql.py
from dask_sql import Context
import pandas as pd

# Buat DataFrame
df = pd.DataFrame({
    "nama": ["Amrin", "Budi", "Citra"],
    "nilai": [80, 90, 85]
})

# Buat context Dask SQL
c = Context()
c.create_table("siswa", df)

# Query SQL
result = c.sql("SELECT * FROM siswa WHERE nilai > 80")
print(result.compute())
