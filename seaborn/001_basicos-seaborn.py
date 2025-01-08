import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  
import os

os.system('clear')

# Mostrando la primera grafica en seaborn
data = pd.DataFrame({'Categoria': ['A', 'B', 'C'], 'Valor': [1, 3, 2]})

plt.switch_backend('TkAgg')  # o plt.switch_backend('QtAgg')

#  sns.set(style='dark',palette='dark',font_scale=1)
#  sns.barplot(x='Categoria', y='Valor', data=data)
#  plt.show()

tip = sns.load_dataset('tips')
#  print(tip)
#  print(type(tip))
#  tip.to_csv('tip.csv', index=False, encoding='utf-8')
#
#  sns.displot(data=tip, x='total_bill',y='tip', hue='sex')
#  sns.displot(data=tip, x='total_bill',hue='sex', kind='kde',legend=False,palette='dark',alpha=0.5)
#  plt.show()

#  sns.histplot(data=tip, x='tip', bins=5, cumulative=True, hue='sex', stat='frequency')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='probability')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent',multiple='dodge')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent',multiple='stack')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent',multiple='fill')
#  sns.kdeplot(data=tip, x='tip', hue='sex', cumulative=False,shade=True)
#  sns.kdeplot(data=tip, x='tip', hue='sex', cumulative=True,shade=False)
#  sns.ecdfplot(data=tip, x='tip', hue='sex')
#  sns.ecdfplot(data=tip, x='tip', hue='sex',stat='count')
#  sns.displot(data=tip, x='tip', hue='sex', kind='kde')
sns.displot(data=tip, x='tip', hue='sex', kind='hist',multiple='stack')
plt.show()
