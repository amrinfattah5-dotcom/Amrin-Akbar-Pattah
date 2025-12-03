import pandas as pd
import dask.dataframe as dd
import itertools

# Contoh DataFrame Pandas
pdf = pd.DataFrame({
    'group': ['A', 'B', 'A', 'B', 'C', 'A'],
    'value': [1, 2, 3, 4, 5, 6],
    'category': ['x','x','y','y','x','y']
})

ddf = dd.from_pandas(pdf, npartitions=2)

# Definisikan custom aggregation
custom_list = dd.Aggregation(
    name='to_list_unique',
    chunk=lambda s: s.apply(lambda x: list(set(x))),  # tiap partisi: set -> list
    agg=lambda s: s.apply(lambda chunks: list(set(itertools.chain.from_iterable(chunks))))
)

# Gunakan groupby + custom agg
result = ddf.groupby('group').agg({
    'value': 'sum',               # contoh aggregasi bawaan
    'category': custom_list       # custom aggregation: unique list dari ‘category’
})

print(result.compute())
