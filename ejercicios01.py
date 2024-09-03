import os
import numpy as np

# Ejercicio 1: Crear y analizar arrays
# Declara un array bidimensional con los números del 1 al 6 en dos filas.
arr_bi = np.array([[1,2,3],[4,5,6]])
print(arr_bi)

# Usa .ndim para verificar el número de dimensiones del array.
print(arr_bi.ndim)

# Usa .shape para verificar el tamaño de las dimensiones del array.
print(arr_bi.shape)

# Usa .dtype para verificar el tipo de datos de los elementos en el array.
print(arr_bi.dtype)

# Ejercicio 2: Conversiones de tipos de datos
# Crea un array unidimensional con un solo elemento de valor 15, usando dtype=np.uint16.
A_u = np.array([15],dtype=np.uint16)
print(A_u.dtype)

# Convierte este array a un array de tipo float32 usando astype y verifica el tipo de datos del nuevo array.
A_u_32 = A_u.astype(np.float32)
print(A_u_32.dtype)

# Crea un array de números enteros y conviértelo a un array de números complejos.
M_ne = np.random.randint(1,8,size=(2,3))
print(M_ne.dtype)
M_nc = M_ne.astype(np.complex64)
print(M_nc.dtype)


# Ejercicio 3: Exploración de tipos de datos
# Crea un array con valores de 8 bits con signo (int8) y otro con enteros de 16 bits sin signo (uint16). Suma ambos arrays y observa el resultado.
M_8_cs = np.random.randint(-10,11,size=(3,3))
M_8_cs = M_8_cs.astype(np.int8)
print(M_8_cs)
M_16_ss = np.random.randint(1,10,size=(3,3))
M_16_ss = M_16_ss.astype(np.uint16)
print(M_16_ss)
Result = M_8_cs+M_16_ss
print(Result)

# Crea un array de 3x3 con números de punto flotante de precisión simple (float32) y otro con precisión doble (float64). Multiplica ambos arrays y verifica el tipo de datos del resultado.
M_pf_ps = np.random.randint(-10,10,size=(3,3)).astype(np.float32)
M_pf_pd = np.random.randint(0,10,size=(3,3)).astype(np.float64)
multi = M_pf_ps*M_pf_pd
print(multi)


# Crea un array con 4 números complejos usando complex128. Multiplica todos los elementos del array por 2 y observa el resultado.


# Ejercicio 4: Cálculos estadísticos en arrays
# Crea un array bidimensional con los valores [2, 4, 6], [8, 10, 12].

# Calcula la suma de todos los elementos del array.

# Calcula la media de los elementos del array.

# Calcula la desviación estándar de los elementos del array.

# Calcula la suma de cada columna del array.


# Ejercicio 5: Indexación y Slicing en arrays unidimensionales
# Declara un array unidimensional con los elementos [5, 10, 15, 20, 25].

# Imprime los primeros cuatro elementos del array.

# Imprime el penúltimo elemento del array.

# Crea un array booleano que indique cuáles elementos son mayores que 12 e imprime el resultado.


# Ejercicio 6: Indexación y Slicing en matrices
# Genera una matriz 4x4 con enteros aleatorios entre 1 y 20.

# Imprime el elemento en la fila 3, columna 2.

# Imprime los primeros dos elementos de cada una de las últimas tres columnas.

# Usa slicing para crear un subarray con las primeras dos filas y las primeras dos columnas de la matriz.


# Desafío adicional
# Genera una matriz 5x5 con enteros aleatorios entre 10 y 50.

# Calcula la media de todos los elementos en las primeras dos filas y las primeras dos columnas.

# Encuentra el número más grande de la última columna.

# Crea un array booleano que indique si cada elemento de la matriz es mayor que 30, y usa este array para filtrar e imprimir los elementos que cumplen la condición.
    
