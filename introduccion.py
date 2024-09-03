import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.system('clear')

escalar = np.array([42])
#  print(escalar)

vector = np.array([30, 29, 42, 35, 31, 33, 36, 42])
#  print(vector)

matrix = np.array([[10,2,3],[4,5,6],[7,8,9]])
#  print(matrix)

tensor = np.array([[[1,2],[3,4],[4,5],[7,8]]])

# Crear un tensor 3x3x3
#  tensor = np.array([[[1, 2, 3],
                   #   [4, 5, 6],
                   #   [7, 8, 9]],
                   #
                   #  [[10, 11, 12],
                   #   [13, 14, 15],
                   #   [16, 17, 18]],
                   #
                   #  [[19, 20, 21],
                   #   [22, 23, 24],
                   #   [25, 26, 27]]])
                   #
#  print(tensor)


#  array_arange = np.arange(10)   # Genera números del 0 al 10
#  print(array_arange)
#
#  eye_matrix = np.eye(6)
#  print(eye_matrix)
#
#  diag = np.diag([1,2,3,4,5,6,7])

#  randon = np.random.random((2,3))
#  print(randon)

#  array = np.array([[1,2,3],[4,5,6]])
#  print(array)
#  print(array.ndim)
#  print(array.shape)
#  print(array.dtype)

#  sum = np.sum(array)
#  print(sum)

#  mean = np.mean(array)
#  print(mean)

#  std = np.std(array)
#  print(std)


#  array = np.array([10, 20, 30, 40, 50])
#  print(array[0:2+1])
#  print(array[-1])
#  bool_index = array > 25
#  print(bool_index)
#  print(type(bool_index))
#
#  array = np.random.randint(1,10,size=(3,3))
#  print(array)
#  print(array[0,1])
#  print(array[:3,:2])
#
#  array = np.array([10, 20, 30, 'hola', 50],dtype=object)
#  for elemento in array:
#      print(type(elemento))
#      print(elemento)
#
# Ejercicios personales
array = np.array([15,25,35,45,55])
#  print(array[0:2])
#  print(array[0])
#  print(array[-1])
bool = array > 30
tipo = bool.array(bool,dtpy=object)
print(tipo)
