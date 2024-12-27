import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

os.system('clear')

def categorize_quantity(df):
    df['Category'] = df['Quantity'].apply(
        lambda x: 'Low' if x <= 20
        else 'Medium' if 20 < x <= 100
        else 'High' 
    )
    return df

# Cargar el dataset
file_path = '~/numpy_pandas_matplotlib/proyecto_platzi/Online_Retail.csv'
#  file_path = '~/Documents/numpy_pandas_matplotlib/proyecto_platzi/Online_Retail.csv'
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
    print('-'*100)

# Limpieza de datos
data_cleaned = data.drop_duplicates()
data_cleaned = data_cleaned.dropna(subset=['CustomerID'])
#  print(data_cleaned)
#  print(data_cleaned.isnull().sum())
#  print('impresion de duplicated')
#  print(data_cleaned.duplicated().sum())
#
# Creacion de columnas
#  print(data_cleaned.head())
data_cleaned['TotalAmount'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']
#  print(data_cleaned.head())
data_cleaned['InvoiceDate'] = pd.to_datetime(data_cleaned['InvoiceDate'])
#  print(data_cleaned.head())
#  print(data_cleaned.info())
data_cleaned['Year'] = data_cleaned['InvoiceDate'].dt.year
data_cleaned['Month'] = data_cleaned['InvoiceDate'].dt.month
#  print(data_cleaned.head())
sales_by_year = data_cleaned.groupby('Year')['TotalAmount'].sum()
#  print(sales_by_year)
data_cleaned['Semester'] = data_cleaned['Month'].apply(lambda x:1 if x<=6 else 2)
sales_by_semester = data_cleaned.groupby(['Year', 'Semester'])['TotalAmount'].sum()
#  print(sales_by_semester)

# Hallar las ventas trimestrales 
data_cleaned['Trimester'] = data_cleaned['Month'].apply(
    lambda x: 1 if x > 0 and x <= 3 
    else 2 if x > 3 and x <= 6 
    else 3 if x > 6 and x <= 9 
    else 4 if x > 9 and x <= 12 
    else None  # Maneja casos fuera del rango 1-12
)
sales_by_trimester = data_cleaned.groupby(['Year', 'Trimester'])['TotalAmount'].sum()
#  print(sales_by_trimester)

# Hallar ventas por mes
sales_by_month = data_cleaned.groupby(['Year', 'Month'])['TotalAmount'].sum()
 
# Visualisacion de datos
# Ejemplo 1
total_returns = data_cleaned[data_cleaned['Quantity'] < 0].shape[0]
#  print(f'Devoluciones totales = {total_returns}')
total_non_returns = data_cleaned[data_cleaned['Quantity'] >= 0].shape[0]
#  print(f'Productos totales = {total_non_returns}')
labels = ['Devoluciones', 'No devoluciones']
sizes = [total_returns, total_non_returns]
color = ['lightcoral', 'lightgreen']
#  plt.figure(figsize = (8,8))
#  plt.pie(sizes, labels=labels, colors=color, startangle=140)
#  plt.title('Porcentaje de trasacciones con y sin devolucion')
#  plt.show()

# Ejemplo 2 con otra grafica de pastel 
# Categorizar productos
data_categorized = categorize_quantity(data_cleaned)
#  percent_cat = data_categorized['Category'].value_counts(normalize=True)*100
#  percent = percent_cat.to_numpy(percent_cat)
#  print(percent)
#  labels = ['Low', 'Medium', 'High']
#  color = ['lightcoral', 'lightgreen']
#  plt.figure(figsize = (8,8))
#  plt.pie(percent, labels=labels, autopct='%1.1f%%', colors=color, startangle=140)
#  plt.title('Categoria en porcentaje')
#  plt.show()

# Ejemplo 3 distrución de ventas por mes y año segun el numero de categorias
category_month_year = data_categorized.groupby(['Month', 'Year'])['Category'].count()
value_list = category_month_year.values.tolist()  # Convierte los valores en una lista.
index_list = category_month_year.index.to_list()  # Convierte los índices (Month, Year) en una lista.
years = [year[1] for year in index_list]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec-2010", "Dec-2011"]

# Crear la gráfica de barras
plt.figure(figsize=(12, 6))
plt.bar(months, value_list, color='skyblue')

# Personalizar
plt.title("Ventas por mes y año")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.xticks(rotation=45)

# Mostrar la gráfica
plt.tight_layout()
plt.show()


