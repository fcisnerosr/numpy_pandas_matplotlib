import os
import numpy as np
import matplotlib.pyplot as plt

os.system('clear')


# Figura 1
#  month = np.array(['E', 'F', 'M', 'A', 'Ma'])
#  sales = np.array([20,25,30,28,35])
#
#  plt.figure(figsize=(8,6))
#
#  plt.plot(month,sales, marker='o', color='blue')
#  plt.title('Ventas mensuales de un producto')
#  plt.xlabel('Meses')
#  plt.ylabel('Ventas en miles de unidades')
#  plt.show()


# Figura 2
#  hours = [2,3,4,5,6,7,8]
#  exam = [55,60,65,70,75,80,85]
#
#  plt.scatter(hours,exam,color='green')
#  plt.title('Relacion entre horas estudiadas y el puntaje en examenes')
#  plt.xlabel('Horas')
#  plt.ylabel('Puntaje')
#
#  plt.show()
#
# Personalización de figuras
#  hours = [2,3,4,5,6,7,8]
#  exam_scores_student_1 = [55,60,65,70,75,80,85]
#  exam_scores_student_2 = [50,58,63,69,74,78,83]
#
#  # Crear grafico de dispersion de dos estudiantes
#  #  plt.scatter(hours, exam_scores_student_1, marker='o', color='green', linestyle='-', label='Estudiante 1')
#  #  plt.scatter(hours, exam_scores_student_2, marker='o', color='red', linestyle='--', label='Estudiante 2')
#  plt.plot(hours, exam_scores_student_2, marker='s', color='blue', linestyle='--', linewidth=2, label='Estudiante 2')
#  plt.plot(hours, exam_scores_student_1, marker='o', color='red', linestyle='--', linewidth=2, label='Estudiante 2')
#  plt.title('Relacion entre horas estudiadas y el puntaje en examenes')
#  plt.xlabel('Horas')
#  plt.ylabel('Puntaje')
#
#  plt.legend()
#  plt.show()

#  categories = ['Producto A', 'Producto B', 'Producto C']
#  sales = [120, 150, 90]
#  # Barras verticales
#  plt.barh(categories, sales, color='skyblue', label='Ventas mensales')
#  #  plt.bar(categories, sales, color='skyblue', label='Ventas mensales')
#  #  plt.annotate(
#  #      'Máximo de ventas',
#  #      xy=('Producto B', 150), xytext=('Producto C', 160),
#  #      arrowprops=dict(facecolor='black', shrink=0.05)
#  #  )
#  plt.title('Ventas de productos en un mes')
#  plt.ylabel('Productos')
#  plt.xlabel('Ventas')
#  plt.legend()
#  plt.show()

# Graficas de barras y de pastel
#  products = ['Producto A', 'Producto B', 'Producto C']
#  market_share = [50, 35, 15]
#  plt.pie(
#      market_share,
#      labels=products,
#      autopct='%1.1f%%',
#      startangle=140,
#      colors=['gold', 'lightcoral', 'orange']
#  )
#  plt.title('Participación de Mercado por Producto')
#  plt.axis('equal')
#  plt.show()

# Histogramas
#  data = np.random.normal(170, 10, 200)
#  plt.hist(data, color='salmon', bins=10, edgecolor='black', alpha=0.6)
#  plt.title('Distribucion de alturas')
#  plt.xlabel('Altura (cm)')
#  plt.ylabel('Densidad')
#  plt.show()

np.random.seed(0)

ages = [np.random.normal(35, 5, 200),
        np.random.normal(40, 5, 200),
        np.random.normal(35, 5, 200)]
#  print(ages)
plt.boxplot(ages, patch_artist=True, notch=False, vert=True, tick_labels=['Grupo 1', 'Grupo 2', 'Grupo 3'])
plt.title('Distribución de edades por grupo')
plt.xlabel('Grupo')
plt.ylabel('Edad (años)')
plt.show()


