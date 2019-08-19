# to get result faster, use the unbuffered (raw) interface, using bytearrays, and doing our own buffering

import dask.dataframe as dd
from itertools import (takewhile, repeat)
from functools import partial

def rawincount(filename):
    f = open(filename, 'rb')
    # bufgen = takewhile(lambda x: x, (f.raw.read(1024 * 1024) for _ in repeat(None)))
    # or
    bufgen = iter(partial(f.raw.read, 1024 * 1024), b'')
    return sum(buf.count(b'\n') for buf in bufgen )
   
filename = 'bigfile.csv'
df = dd.read_csv(filename)
df_shape = (rawincount(filename) - 1, len(df.columns))
print(f"Shape: {df_shape}")   
