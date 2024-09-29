import pandas as pd
import numpy as np
import os
os.system('clear')

path = 'Online_Retail.csv'
df = pd.read_csv(path,encoding='windows-1252')
#  data_excel = pd.read_excel(path)
#  data_json = pd.read_json(path)

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
dt_from_array = pd.DataFrame(array,columns=['A','B','C'])

list = [[1,'Jhon',22],[2,'Anna',24]]
df_from_list = pd.DataFrame(list,columns=['ID','Name','Age'])

dicc = [{'ID':1,
    'Name':'Jhon',
    'Age':22},
    {'ID':2,
    'Name':'Ana',
    'Age':24}]
df_from_dicc = pd.DataFrame(dicc,columns=['ID','Name','Age'])

