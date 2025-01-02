import re
import pandas as pd
import os
os.system('clear')

# Lee el archivo .txt
with open('001_gastos_2024.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Lista para almacenar los datos extraídos
data = []
#
#  # Expresión regular para extraer los datos deseados
pattern = r'([\d.]+),\s?([\w\sáéíóúÁÉÍÓÚñÑ]+),\s?(.+?),\s?([\w\sáéíóúÁÉÍÓÚñÑ]*)'

# Procesa cada línea del archivo
for line in lines:
    match = re.search(pattern, line)
    if match:
        # Extrae los valores según la expresión regular
        #  date = match.group(1)  # Fecha
        amount = match.group(1)  # Cantidad
        category = match.group(2).strip()  # Tipo de gasto
        description = match.group(3).strip()  # Descripción
        payment = match.group(4).strip()  # Forma de pago

        # Agrega los datos extraídos a la lista
        data.append([amount, category, description, payment])

# Convierte los datos en un DataFrame
df1 = pd.DataFrame(data, columns=['Cantidad', 'Tipo de gasto', 'Descripción', 'Forma de pago'])

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Limpieza de datos
df1['Forma de pago'] = df1['Forma de pago'].str.replace(r'tdc|Tdc|Transferencia|transferencia', 'debito', regex=True)
df1['Forma de pago'] = df1['Forma de pago'].str.replace(r'crédito', 'credito', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'bebé', 'bebe', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'formación', 'formacion', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'fummigación', 'fumigacion', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'jardín', 'jardin', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'despnesa', 'despensa', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'medicinas', 'medicina', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'preapracion', 'preparacion', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'ultrasonidos', 'bebe', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'comida fuera del hogar', 'comidas fuera del hogar', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'bici', 'bicicleta', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'envoltura', 'regalos', regex=True)
df1['Tipo de gasto'] = df1['Tipo de gasto'].str.replace(r'bicicletacleta', 'bicicleta', regex=True)

# Concatenacion de fechas
pattern = r'(\d\d/\d\d/\d{4})'
data_date = []
for line in lines:
    match = re.search(pattern, line)
    if match:
        date = match.group(1)
        data_date.append([date])
df_from_array = pd.DataFrame(data_date) 

df = pd.concat([df1, df_from_array], axis=1) 
df.rename(columns={0:'Fecha'},inplace=True)
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
#  df['Fecha'] = df['Fecha'].dt.strftime('%d-%m-%Y')
df['Cantidad'] = pd.to_numeric(df['Cantidad'], errors='coerce')
print(df)


# Agrupaciones 
df.set_index('Fecha', inplace=True)
df['Month'] = df.index.month
#  print(df)

#  # Visualizacion completa del df en csv
#  ruta = '~/numpy_pandas_matplotlib/proyecto_gastos/df.csv'
#  df.to_csv(ruta, index=False, encoding='utf-8')

sales_cat = df.groupby(['Tipo de gasto', 'Month'])['Cantidad'].sum().reset_index()
print(sales_cat)


