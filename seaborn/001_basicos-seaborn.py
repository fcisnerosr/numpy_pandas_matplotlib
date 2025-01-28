import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd  
import os

os.system('clear')

  ruta = os.path.expanduser("~/Documents/sheets/data_science/001_numpy_pandas_matplotlib_seaborn/graficas_seaborn")
#  ruta_completa = os.path.join(ruta, "010_dodge_swarm_plots_arragend_in_a_grid_layout_based_on_another_categorical_variable.png")
#  plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")

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


#  sns.histplot(data=tip, x='tip', bins=5, cumulative=True, hue='sex', stat='frequency')

#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='probability')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue=':xsex', stat='percent')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent',multiple='dodge')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent',multiple='stack')
#  sns.histplot(data=tip, x='tip', bins=15, cumulative=False, hue='sex', stat='percent',multiple='fill')
#  sns.kdeplot(data=tip, x='tip', hue='sex', cumulative=False,shade=True)
#  plt.show()

#  sns.kdeplot(data=tip, x='tip', hue='sex', cumulative=True,shade=False)
#  sns.ecdfplot(data=tip, x='tip', hue='sex')
#  sns.ecdfplot(data=tip, x='tip', hue='sex',stat='count')
#  sns.displot(data=tip, x='tip', hue='sex', kind='kde')
#  sns.displot(data=tip, x='tip', hue='sex', kind='hist',multiple='stack')
#  plt.show()

#  #  Variables categoricas
#  sns.countplot(data=tip,y='day',hue='sex')
#  sns.stripplot(data=tip,x='day',hue='sex')
#  sns.stripplot(data=tip,x='day',y='total_bill',hue='sex')
#  sns.stripplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True)
#  sns.swarmplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True)
#  sns.boxplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True)
#  plt.show()
#
# Combinacion de ambas graficas, swarmplot y boxplot
#  plt.figure(figsize=(6,6))
#  sns.swarmplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True,color='0',marker='<')
#  sns.boxplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True)

#  plt.show()

#gg
#  plt.figure(figsize=(6,6))
#  sns.violinplot(data=tip,x='day',y='total_bill',hue='sex',split=True,dodge=True,palette='pastel')

#
#  sns.catplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True,kind='box',col='time')
#  sns.catplot(data=tip,x='day',y='total_bill',hue='sex',dodge=True,kind='swarm',col='time')
#  plt.show()

#  plt.figure(figsize=(8,6))
#  markers = {'Lunch':'D','Dinner':'s'}
#  sns.scatterplot(data=tip,x='total_bill',y='tip',hue='day',style='time',size='size',markers=markers)
#  plt.legend(loc='center',bbox_to_anchor=(1.09,0.5))
#  ruta = os.path.expanduser("~/Documents/sheets/data_science/001_numpy_pandas_matplotlib_seaborn/graficas_seaborn")
#  ruta_completa = os.path.join(ruta, "010_dodge_swarm_plots_arragend_in_a_grid_layout_based_on_another_categorical_variable.png")
#  plt.savefig(ruta_completa, dpi=300, bbox_inches="tight")
#  plt.show()
#
#  sns.lineplot(data=tip,x='total_bill',y='tip')
#  plt.show()
#
#  markers = {'Lunch':'d','Dinner':'s'}
#  sns.relplot(data=tip,x='total_bill',y='tip',hue='day',style='time',size='size',markers=markers,height=6,aspect=1.3)
#  013_two_variable_scatter
#  plt.show()
#
#  sns.jointplot(data=tip, x='total_bill',y='tip')
#  sns.jointplot(data=tip, x='total_bill',y='tip',hue='sex')
#  sns.jointplot(data=tip, x='total_billusy='tip',hue='sex',kind='hist')
#  sns.jointplot(data=tip, x='total_bill',y='tip',hue='sex',kind='kde')
#  sns.jointplot(data=tip, x='total_bill',y='tip',hue='sex',kind='hist',marginal_ticks=True,marginal_kws=dict(bins=25,fill=False,multiple='dodge'))
#  plt.show()
#
#  #  Pairplot (relaciones de variables numericas en distintas graficas)
#  sns.pairplot(data=tip)
#  sns.pairplot(data=tip,hue='sex',kind='scatter')
#  plt.show()

# heatmap
print(tip)
numeric_columns = tip.select_dtypes(include=['number']).columns
tip_numeric = tip[numeric_columns]
correlation_matrix = tip_numeric.corr()
print(correlation_matrix)
#  sns.heatmap(correlation_matrix)
#  plt.show()
# impresion de grafico. Correlación numerica entre variables numericas
#  sns.heatmap(correlation_matrix, annot=True)
#  plt.show()
# impresion de grafico. Correlación numerica entre variables numericas pero con dato fraccionario impreso
sns.heatmap(correlation_matrix, annot=True,cmap='coolwarm',linewidths=5)
