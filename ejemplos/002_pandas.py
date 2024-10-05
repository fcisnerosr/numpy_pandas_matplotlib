import pandas as pd
import numpy as np
import os
os.system('clear')

path = '~/Documents/numpy_pandas_matplotlib/Online_Retail.csv'
df = pd.read_csv(path,encoding='windows-1252')
num_rows, num_columns = df.shape
print(df.columns)
price = df['UnitPrice']
print(df.tail())
#  print(price)
#  mean = price.mean()
#  print(mean)
#  suma = price.sum()
#  print(suma)
#  print(f'filas = {num_rows}')
#  print(f'columnas = {num_columns}')
#  print(df)
#  print(df.head())
#  print(df.head(8))
#  print(df.sample(2))
#  print(df.tail())
#  print(df.columns)
series_priced = df['Quantity']
#  print(series_priced)
#  print(series_priced[1])
summary = df.describe()
#  print(summary)
mean = series_priced.mean()
#  print(f'La media es: {mean}')
mediana = series_priced.median()
#  print(f'La mediana es: {mediana}')
suma = series_priced.sum()
#  print(f'La suma es: {suma}')
count = series_priced.count()
#  print(f'La cuenta es: {count}')
#  data_excel = pd.read_excel(path)
#  data_json = pd.read_json(path)

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
dt_from_array = pd.DataFrame(array,columns=['A','B','C'])

list = [[1,'Jhon',22],[2,'Anna',24]]
df_from_list = pd.DataFrame(list,columns=['ID','Name','Age'])

dicc = [{'ID':1,
    'Name':'Jhon',
    'Age':22},
    {'ID':2,
    'Name':'Ana',
    'Age':24}]
df_from_dicc = pd.DataFrame(dicc,columns=['ID','Name','Age'])
#  print(df_from_dicc)
#  print(df_from_dicc.columns)

#  columns = df.columns
#  print(columns)
