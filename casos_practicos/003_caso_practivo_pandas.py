import pandas as pd
import os
os.system('clear')
import numpy as np

path = '~/numpy_pandas_matplotlib/casos_practicos/Example_DataFrame.csv'
df = pd.read_csv(path,encoding='windows-1252')
print(df)
#  print(df.head())
Unit_Price = df['Unit_Price']
print(Unit_Price)
