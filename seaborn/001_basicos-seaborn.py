import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  

# Crear un DataFrame con los datos
data = pd.DataFrame({'Categoria': ['A', 'B', 'C'], 'Valor': [1, 3, 2]})
print(data)

sns.set(style='dark',palette='dark',font_scale=1)
sns.barplot(x='Categoria', y='Valor', data=data)
plt.show()
