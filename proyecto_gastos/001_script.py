import re
import pandas as pd
import os
import matplotlib.pyplot as plt
from utils import aplicar_reemplazos

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

print(df1)



# Limpieza de datos
replacements = {
    'tdc|Tdc|Transferencia|transferencia': 'debito',
    'crédito': 'credito',
    'bebé': 'bebe',
    'formación': 'formacion',
    'fumigación|fumigacion': 'fumigacion',
    'jardín': 'jardin',
    'despensa|despnesa': 'despensa',
    'medicinas|medicina': 'medicina',
    'preapracion|preparación': 'preparacion',
    'ultrasonidos': 'bebe',
    'comida fuera del hogar': 'comidas fuera del hogar',
    'celular': 'otros',
    'envoltura|regalos': 'regalos',
    'bici': 'bicicleta',
    'garrafones|despensa': 'despensa',
    'viajes|viaje|viajess': 'viajes',
    'lavanderia': 'limpieza',
    'fumigación': 'fumigacion',
    'membrecia sams': 'otros',
    'tramites': 'otros',
    'microsoft': 'otros'
}

df1 = aplicar_reemplazos(df1, 'Tipo de gasto', replacements)
df1 = df1.drop_duplicates()

# Visualizacion completa del df en csv
ruta = '~/numpy_pandas_matplotlib/proyecto_gastos/df1.csv'
df1.to_csv(ruta, index=False, encoding='utf-8')
#
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
#  print(df)


# Agrupaciones
df.set_index('Fecha', inplace=True)
df['Month'] = df.index.month
#  print(df)

sales_cat = df.groupby(['Tipo de gasto', 'Month'])['Cantidad'].sum().reset_index()

sales_cat['Percentage'] = sales_cat['Cantidad'] / sales_cat.groupby('Month')['Cantidad'].transform('sum') * 100
print(sales_cat)

df_pivot = sales_cat.pivot(index='Month', columns='Tipo de gasto', values='Percentage')
#  print(df_pivot)



# Graficas
df_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Distribución de gastos por mes', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Cantidad', fontsize=14)
plt.legend(title='Tipo de gasto', fontsize=10)
plt.xticks(rotation=0)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
