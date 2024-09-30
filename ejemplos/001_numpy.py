import numpy as np
#  import pandas as pd
#  import matplotlib.pyplot as plt
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

# Clase 6. Broadcasting y operaciones lógicas e Numpy
#  prices = np.array([100,200,300])
#  discount = np.array([0.9])
#  discount_prices = prices*discount
#  print(discount_prices)
#  prices = np.random.randint(100,500,size=(3,3),dtype=np.int64)
#  discount = np.array([10,20,30])
#  discount_prices = prices-discount
#  print(prices)
#  print(discount_prices)

#  array = np.array([1,2,3,4,5])
#  print(np.all(array > 3))
#  print(np.any(array > 3))
#
#  array_a = np.array([1,2,3])
#  array_b = np.array([4,5,6])
#  concatenated = np.concatenate((array_a,array_b))
#  print(concatenated)
#
#  satecked_v = np.vstack((array_a,array_b))
#  print(satecked_v)
#
#  stacked_h = np.hstack((array_a,array_b))
#  print(stacked_h)
#
#  array_c = np.arange(1,15+1)
#  print(array_c)
#  split_array = np.split(array_c,5)
#  print(split_array)

#  survey_responses = np.array(["excelente","bueno","bueno","excelente","malo","bueno","bueno","excelente"])
#  print(survey_responses)
#  unique_elements, counts = np.unique(survey_responses,return_counts=True)
#  print(unique_elements)
#  print(counts)

#  array_x = np.arange(10+1)
#  print(array_x)
#  view_array = array_x[0:5]
#  array_x[0:2+1] = [9,9,9]
#  print(array_x)
#  print(view_array)

#  array_x = np.arange(10+1)
#  copy_x = array_x[[0,1]]
#  array_x[0:1+1] = [10,10]
#  print(copy_x)
#  print(array_x)

matrix = np.array([[1,2],[4,5],[6,9]])
print(matrix)
matrixT = matrix.T
print(matrixT)

A = np.arange(1,50+1)
reshaped_A = A.reshape(5,10)

vector = np.arange(9+1)
print(vector)
vector_reberse = vector[::-1]
print(vector_reberse)

matrix = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
flattened_matrix = matrix.flatten()
print(matrix)
print(flattened_matrix)

# Suma
A = np. array([[1,2],[3,4]])
B = np. array([[5,6],[7,8]])
suma = A+B

# Multiplicar
product = np.dot(A,B)

A = np. array([[1,2],[3,4]])
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

# Resolver Ax = b
b = np.array([9,11])
x = np.linalg.solve(A,b)
