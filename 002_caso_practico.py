import numpy as np
import os
os.system('clear')

# Funciones
def sum_mean(ventas,nombre_ventas):
    sum = np.sum(ventas)
    mean = np.mean(ventas)
    print(f'La suma del {nombre_ventas} es {sum} y su media es {mean}')
    
def indexf(mes_input,meses):
    index = 0
    for mes in meses:
        if mes == mes_input:
            break
        else:
            index = index+2
    return index

def ventas_index(mes_input,ventas,meses):
    index = indexf(mes_input,meses)
    venta_mes_index = ventas[index]
    return venta_mes_index

#  def media_mes_index(mes_input,ventas):

# Paso 1: Crear arrays con datos de ventas mensuales
# Crea un array de meses.
# Crea tres arrays: ventas_A, ventas_B, ventas_C con los datos de ventas mensuales para cada producto.
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
ventas_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
ventas_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
ventas_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])

# Paso 2: Transformaciones básica
# Calcula la media y la suma de las ventas para cada producto A, B, y C.
# Imprime los resultados.
sum_mean(ventas_A,"Ventas A")
sum_mean(ventas_B,"Ventas B")
sum_mean(ventas_C,"Ventas C")

# Paso 3: Manipulación y análisis de datos
# Calcula el total de las ventas dado un mes determinado
mes_input = 'Marzo'
ventas_mes_A = ventas_index(mes_input,ventas_A,meses)
ventas_mes_B = ventas_index(mes_input,ventas_B,meses)
ventas_mes_C = ventas_index(mes_input,ventas_C,meses)
suma_mes_3 = ventas_mes_A+ventas_mes_B+ventas_mes_C
print(f'La suma de los 3 ventas de {mes_input} es {suma_mes_3}')

# Imprime el total de ventas por mes, el promede ventas por producto, y los meses con mayor y menor ventas.
# Calcula el total de ventas por mes sumando las ventas de los tres productos.
stacked_v = np.vstack((ventas_A,ventas_B,ventas_C))
print(stacked_v)
largo_fila = np.arange(len(ventas_A))
vector_sum = np.zeros(len(ventas_A))
for col in largo_fila:
    vector_sum[col] = np.sum(stacked_v[:,col])
print(vector_sum)
    
# Calcula el promedio de ventas por producto.
largo_col = np.arange(stacked_v.shape[0])
print(largo_col)
vector_mean = np.zeros(len(largo_col))
for fila in largo_col:
    vector_mean[fila] = np.mean(stacked_v[fila])
print(vector_mean)

# Identifica el mes con mayor y menor ventas usando las funciones adecuadas de NumPy.
valor_mayor = np.max(vector_sum)
valor_menor = np.min(vector_sum)
print(largo_fila)
for num in largo_fila:
    if valor_mayor == vector_sum[num]:
        print(f'Mes con mayor ventas: {meses[num]}. Ventas = {valor_mayor}')
    elif valor_menor == vector_sum[num]:
        print(f'Mes con menor ventas: {meses[num]}. Ventas = {valor_menor}')

# Paso 4: Operaciones avanzadas con NumPy
# Crea una matriz de ventas con ventas_A, ventas_B, y ventas_C.
stacked_v = np.vstack((ventas_A,ventas_B,ventas_C))
print('Matriz de ventas concatenada:')
print(stacked_v)
# Reorganiza la matriz con reshape en una nueva estructura de 3x4x3.
ventas_reshaped = stacked_v.reshape(3,4,3)
#  print(f'ventas_reshaped = {ventas_reshaped}')
# Transpón la matriz de ventas.
ventas_reshaped_T = stacked_v.T
#  print(f'ventas_transpuesta = {ventas_reshaped_T}')

# Imprime la matriz original, la matriz reorganizada, y la matriz transpuesta.
# Invertir arrays y aplanar matrices
reversed_ventas_stacked_v = np.flip(stacked_v)
# print(reversed_ventas_stacked_v)

# Invierte el orden de los elementos en cada fila de la matriz de ventas.
matriz_filas_invertidas = np.zeros((3,12))
for fila in largo_col:
    fila_matriz = stacked_v[fila,:]
    fila_inv = np.flip(fila_matriz)
    for col in largo_fila:
        matriz_filas_invertidas[fila,col] = fila_inv[col]
    
# Aplana la matriz en un array unidimensional.
matriz_filas_invertidas_flat = matriz_filas_invertidas.flatten()
print(matriz_filas_invertidas_flat)

# Paso 5: Análisis de elementos únicos y sus conteos
# Usa np.unique para obtener los elementos únicos y sus conteos de la matriz aplanada.
# Imprime los elementos únicos y sus conteos.
mat_unique_flat = np.unique(matriz_filas_invertidas_flat)
print(mat_unique_flat)
unique_elements, counts = np.unique(matriz_filas_invertidas, return_counts=True)
#  # impresion en pantalla
#  index = 0
#  for elements in unique_elements:
#      print(f'{elements} = {counts[index]}')
#      index +=1

#  # diccionario
#  dicc = {}
#  index = 0
#  for elements in unique_elements:
#      dicc[elements] = counts[index]
#      index +=1
#  print(dicc)

# Paso 6: Indexación y slicing
# Selecciona las ventas del primer trimestre (primeras tres columnas) para cada producto.
trimestres = len(meses)/3
ini = 0
for trimestre in range(3,12+1,3):
    print(trimestre)
    ini +=3

# Usa indexación booleana para seleccionar meses con ventas totales superiores a 800.
# Imprime los meses y las ventas superiores a 800.

# Selección avanzada
# Selecciona las ventas de los meses con índices pares (0, 2, 4, 6, 8, 10) para cada producto.
# Imprime las ventas correspondientes a los meses seleccionados.
