import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

os.system('clear')

df = pd.read_excel('~/Documents/numpy_pandas_matplotlib/seaborn/datos_clau/Desinformación_en_la_Alimentación_de_Mujeres_Lactantes_Copia.xlsx')
#Configurar estilo
sns.set_theme(style="whitegrid")

# 1. Histograma de edades
plt.figure(figsize=(8,4))
sns.histplot(df["Edad"], bins=10, kde=True)
plt.title("Distribución de edades")
ruta = os.path.expanduser("~/Documents/numpy_pandas_matplotlib/seaborn/datos_clau")
ruta_completa = os.path.join(ruta, "graf1.png")
plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
#  plt.show()

# 2. Conteo por nivel educativo
plt.figure(figsize=(10,4))
sns.countplot(y=df["Nivel educativo"], order=df["Nivel educativo"].value_counts().index)
plt.title("Distribución por Nivel Educativo")
ruta_completa = os.path.join(ruta, "graf2.png")
plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
#  plt.show()

# 3. Tiempo de lactancia vs. Asesoría profesional
plt.figure(figsize=(8,4))
sns.countplot(x="Tiempo de lactancia (en meses)", hue="¿Recibiste asesoría profesional sobre alimentación en lactancia?", data=df)
plt.title("Relación entre Lactancia y Asesoría Profesional")
ruta_completa = os.path.join(ruta, "graf3.png")
plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
#  plt.show()

# 4. Consumo de suplementos por nivel educativo
plt.figure(figsize=(8,6))
cross_tab = pd.crosstab(df["Nivel educativo"], df["¿Consumes suplementos en la lactancia?"])
sns.heatmap(cross_tab, annot=True, cmap="Blues", fmt="d")
plt.title("Consumo de Suplementos según Nivel Educativo")
ruta_completa = os.path.join(ruta, "graf4.png")
plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
#  plt.show()
#
# 5. Fuente de información sobre alimentación
plt.figure(figsize=(8,4))
sns.countplot(y="¿Cuál es tu principal fuente de información?", data=df, order=df["¿Cuál es tu principal fuente de información?"].value_counts().index)
plt.title("Fuente principal de información sobre alimentación")
ruta_completa = os.path.join(ruta, "graf5.png")
plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
#  plt.show()
