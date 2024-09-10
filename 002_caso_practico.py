import numpy as np
import os
os.system('clear')

# Funciones
def sum_mean(ventas,nombre_ventas):
    sum = np.sum(ventas)
    mean = np.mean(ventas)
    print(f'La suma del {nombre_ventas} es {sum} y su media es {mean}')
    
def index():

def ventas_index(mes_input,ventas):
    index = 0
    for mes in meses:
        if mes == mes_input:
            break
        else:
            index = index+2
    venta_mes_index = ventas[index]
    return venta_mes_index

def media_mes_index(mes_input,ventas):
    splash

# Paso 1: Crear arrays con datos de ventas mensuales
# Crea un array de meses.
# Crea tres arrays: ventas_A, ventas_B, ventas_C con los datos de ventas mensuales para cada producto.
meses = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
ventas_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
ventas_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
ventas_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])

# Paso 2: Transformaciones básicas con NumPy
# Calcula la media y la suma de las ventas para cada producto A, B, y C.
# Imprime los resultados.
sum_mean(ventas_A,"Ventas A")
sum_mean(ventas_B,"Ventas B")
sum_mean(ventas_C,"Ventas C")

# Paso 3: Manipulación y análisis de datos
# Calcula el total de ventas por mes sumando las ventas de los tres productos.
# Calcula el promedio de ventas por producto.
# Identifica el mes con mayor y menor ventas usando las funciones adecuadas de NumPy.
# Imprime el total de ventas por mes, el promedio de ventas por producto, y los meses con mayor y menor ventas.
mes_input = 'Febrero'
ventas_mes_A = ventas_index(mes_input,ventas_A)
ventas_mes_B = ventas_index(mes_input,ventas_B)
ventas_mes_C = ventas_index(mes_input,ventas_C)
suma_mes_3 = ventas_mes_A+ventas_mes_B+ventas_mes_C
print(suma_mes_3)



# Paso 4: Operaciones avanzadas con NumPy
# Crea una matriz de ventas con ventas_A, ventas_B, y ventas_C.
# Reorganiza la matriz con reshape en una nueva estructura de 3x4x3.
# Transpón la matriz de ventas.
# Imprime la matriz original, la matriz reorganizada, y la matriz transpuesta.

# Invertir arrays y aplanar matrices
# Invierte el orden de los elementos en cada fila de la matriz de ventas.
# Aplana la matriz en un array unidimensional.
# Imprime la matriz invertida y aplanada.

# Paso 5: Análisis de elementos únicos y sus conteos
# Usa np.unique para obtener los elementos únicos y sus conteos de la matriz aplanada.
# Imprime los elementos únicos y sus conteos.

# Paso 6: Indexación y slicing
# Selecciona las ventas del primer trimestre (primeras tres columnas) para cada producto.
# Usa indexación booleana para seleccionar meses con ventas totales superiores a 800.
# Imprime los meses y las ventas superiores a 800.

# Selección avanzada
# Selecciona las ventas de los meses con índices pares (0, 2, 4, 6, 8, 10) para cada producto.
# Imprime las ventas correspondientes a los meses seleccionados.
