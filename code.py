import pandas as pd
from pathlib import Path
import pyarrow.parquet as pq

path = Path(Path.cwd(), 'data', 'train_series.parquet')
table = pq.read_table(path)
df = table.to_pandas()  # Convert to Pandas DataFrame if needed
print(df.head())
