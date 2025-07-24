import pandas as pd
import os
os.system('clear')
import numpy as np

path = '~/numpy_pandas_matplotlib/casos_practicos/Example_DataFrame.csv'
df = pd.read_csv(path,encoding='windows-1252')
print(df)
#  print(df.head())
Unit_Price = df['Unit_Price']
print(Unit_Price[0])
Country = df['Country']
print(Country[1])
print(df.describe())
Quantity = df['Quantity']
print(Quantity)
suma = Quantity.sum()
print(f'suma = {suma}')
#  print(Country)
#  print(Unit_Price)
#  print(df.columns)
#  print(df.head(2))
count = Quantity.count()
print(f'count = {count}')
print(df)
#  first_row = df.iloc[0]
#  print(first_row)
#  first_five_rows = df.iloc[0:5]
#  print(first_five_rows)
primeras_filas = df.iloc[5:10]
print(primeras_filas)
