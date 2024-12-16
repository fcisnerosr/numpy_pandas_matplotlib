import pandas as pd
import os

os.system('clear')

# Cargar el dataset
#  file_path = '~/numpy_pandas_matplotlib/proyecto_platzi/Online_Retail.csv'
file_path = '~/Documents/numpy_pandas_matplotlib/proyecto_platzi/Online_Retail.csv'
data = pd.read_csv(file_path, encoding='windows-1252')
pd.set_option('display.max_columns', None)
#  print(data.info())
#  print(data.head())
#  #  print(data.describe())
#  print(data.isnull().sum())
#  print(data.duplicated().sum())

unique_values = {col: data[col].unique() for col in data.columns}
for col, values in unique_values.items():
    print(f'Columna: {col}')
    print(f'Numero de valores: {len(values)}')
    print(f'Valores únicos: {values[:10]}')
<<<<<<< HEAD
    print('-'*50)
=======
    print('-'*100)

# Limpieza de datos
data_cleaned = data.drop_duplicates()
data_cleaned = data_cleaned.dropna(subset=['CustomerID'])
print(data_cleaned)
print(data_cleaned.isnull().sum())
print(data_cleaned.duplicated().sum())

# Creacion de columnas
print(data_cleaned.head())
data_cleaned['TotalAmount'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']
print(data_cleaned.head())
data_cleaned['InvoiceDate'] = pd.to_datetime(data_cleaned['InvoiceDate'])
print(data_cleaned.head())
print(data_cleaned.info())
data_cleaned['Year'] = data_cleaned['InvoiceDate'].dt.year
data_cleaned['Month'] = data_cleaned['InvoiceDate'].dt.month
print(data_cleaned.head())

>>>>>>> 7a81 (limpieza de datos y conversion a datos temporales)
