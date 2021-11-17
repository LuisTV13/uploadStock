import pandas as pd
import json
import numpy as np
from datetime import date, datetime

x= '879270990021'
print(x)
print(len(x))


path = 'adjunto/STOCK TODOS LOS ALMACENES AL 12.11.2021.xlsx'
fecha=datetime.today().strftime('%Y-%m-%d')
date ='2021-11-12'
df = pd.read_excel(path,sheet_name='Hoja1')

    #print(df['Fecha Exíración'])
codigoItem = df['Código Item']

# print(codigoItem[1:6])

# print(codigoItem)   
CODITEM =[]
for item in codigoItem:
      k = str(item)
      
      x =k[0:5]
      y=k[5:10]
      z=k[10:12]
      newitem = x+'-'+y+'-'+z
      CODITEM.append(newitem)
print(CODITEM)



    