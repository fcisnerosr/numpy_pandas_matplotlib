import pandas as pd
import numpy as np
import os
os.system('clear')

path = '~/Documents/numpy_pandas_matplotlib/Online_Retail.csv'
path = '~/numpy_pandas_matplotlib/Online_Retail.csv'
df = pd.read_csv(path,encoding='windows-1252')
# print(df)
#  num_rows, num_columns = df.shape
# print(df.columns)
#  price = df['UnitPrice']
# #  print(df.tail())
# #  print(price)
#  mean = price.mean()
# #  print(mean)
#  suma = price.sum()
# #  print(suma)
# #  print(f'filas = {num_rows}')
# #  print(f'columnas = {num_columns}')
# #  print(df)
# #  print(df.head())
# #  print(df.head(8))
# #  print(df.sample(2))
# #  print(df.tail())
# #  print(df.columns)
series_priced = df['Quantity']
# #  print(series_priced)
# #  print(series_priced[1])
summary = df.describe()
# #  print(summary)
mean = series_priced.mean()
# #  print(f'La media es: {mean}')
mediana = series_priced.median()
# #  print(f'La mediana es: {mediana}')
suma = series_priced.sum()
# #  print(f'La suma es: {suma}')
count = series_priced.count()
# #  print(f'La cuenta es: {count}')
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
# #  print(df_from_dicc)
# #  print(df_from_dicc.columns)

#  columns = df.columns
# #  print(columns)

# iloc y loc
first_row = df.iloc[1]
# #  print(first_row)
first_five_rows = df.iloc[:5]
# #  print('primeras 5 filas')
# #  print(first_five_rows)
six_to_eigth_rows = df.iloc[6:8]
# #  print('de las 5 a la 7')
# #  print(six_to_eigth_rows)
# #  print('impresion completa del dataframe')
# #  print(df)
subset = df.iloc[:3,:2] 
# #  print('tres primeras filas, dos primeras columnas')
# #  print(subset)
value = df.iloc[0,4] 
# #  print(value)
# loc
row_index_three = df.loc[3]
# #  print(row_index_three)
row_index_zero_to_four = df.loc[:2]
# #  print(row_index_zero_to_four)
col_date = df.loc[:,'InvoiceDate']
col_stock_date_unitprice_0 = df.loc[0,['StockCode','InvoiceDate','UnitPrice']]
# #  print(col_stock_date_unitprice_0)
col_stock_date_unitprice_02 = df.loc[0:2,['StockCode','InvoiceDate','UnitPrice']]
# #  print(col_stock_date_unitprice_02)
france_unitprice = df.loc[df['Country']=='France',['Country','UnitPrice']]
# #  print(france_col)
france_unitprice_3 = df.loc[df['Country']=='France',['Country','UnitPrice']].head(3)
# print(france_unitprice_3)
france_unitprice_3 = df.loc[df['Country']=='France',['Country','UnitPrice']].tail(3)

# datos faltantes
missing_data = df.isna()
#  print(missing_data.head(10))
missing_data_count = df.isna().sum()
#  print(f'conteo de datos faltantes por columna: \n{missing_data_count}')
no_missing_rows = df.dropna()
#  print(f'datos sin filas con valores faltantes:\n {no_missing_rows}')
no_missing_columnas = df.dropna(axis=1)
#  print(f'datos sin filas con flalores faltantes: \n{no_missing_columnas}')
df_filled_zeros = df.fillna(0)
#  print(df_filled_zeros)
df_filled_zeros_count = df_filled_zeros.isna().sum()
#  print(df_filled_zeros_count)

mean_unit_price = df['UnitPrice'].mean()
df_filled_mean = df['UnitPrice'].fillna(mean_unit_price)
#  print(df_filled_mean)

# Manipulación de columnas
#  print(df)
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
#  print(df.head(10))
df['HighValue'] = df['TotalPrice']>16
#  print(df['HighValue'].head(10))
# Tipos de datos en columnas
#  print(df.info())
#  print(df['InvoiceDate'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M')
#  print(df.info())
#  print(df['InvoiceDate'])
#  print(df['UnitPrice'].head())
df['DiscountedPrice'] = df['UnitPrice'].apply(lambda x:x*0.9)
# funcion para probar applay sobre nuestro dataframe
def categorize_price(price):
    if price > 50:
        return 'High'
    elif price < 20:
        return 'Medium'
    else:
        return 'Low'

df['PriceCategory'] = df['UnitPrice'].apply(categorize_price)
print(df.head(100))

# Groupby
country_cont = df['Country'].value_counts()
#  print(country_cont)
country_group = df.groupby('Country')['Quantity'].sum()
print(country_group)
country_stats = df.groupby('Country')['UnitPrice'].agg(['mean','sum'])
print(country_stats)
country_stock_group = df.groupby(['Country','StockCode'])['Quantity'].sum()
print(country_stock_group)
def total_revenue(group):
    return (group['Quantity'] * group['UnitPrice']).sum()

revenue_per_country = df.groupby('Country').apply(total_revenue)
print(revenue_per_country)
























#  # Crear un DataFrame de ejemplo
#  data = {'name': ['Alice', 'Bob', None, 'Dave', 'Eve'],
#          'age': [24, None, 35, 46, None],
#          'gender': ['F', 'M', 'M', 'M', 'F']}
#  df = pd.DataFrame(data)
#  #  print(df)
#  # Eliminar filas donde al menos un elemento es NaN
#  df_cleaned = df.dropna()
#  print(f'\nDatos limpios \n{df_cleaned}')
