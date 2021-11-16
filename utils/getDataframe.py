import pandas as pd
import json
import numpy as np
from datetime import date, datetime

path = 'adjunto/STOCK TODOS LOS ALMACENES AL 12.11.2021.xlsx'
def getJSONxDataFrame(path):
    fecha=datetime.today().strftime('%Y-%m-%d')
    date ='2021-11-12'
    df = pd.read_excel(path,sheet_name='Hoja1')

    #print(df['Fecha Exíración'])
    codigoItem = df['Código Item']
    CODITEM =[]
    for item in codigoItem:
        CODITEM.append(str(item))
    
    
    fechaIngreso =[]
    for fechaing in codigoItem:
        fechaIngreso.append(str(fecha))
    nombreItem = df['Nombre del Item']
    saldo = df['Saldo']
    SALDO1 =[]
    for sald in saldo:
        SALDO1.append(str(sald))


    codigolocalicacion = df['Código locación']
    fechafifo = df['Fecha Fifo'] 
    FECHAFIFO1 =[]
    for fech in fechafifo:
        FECHAFIFO1.append(str(fech))
        
    fechaExpiracion = df['Fecha Exíración']
    FECHAEXP =[]
    for fech1 in fechaExpiracion:
        FECHAEXP.append(str(fech1))
    NumeroLote = df['Número de Lote']
    Huid = df['HU ID']
    atributo2 = df['Atributo 2']
    atributo6 = df['Atributo 6']
    familia = df['Familia']

    format_json ={
        "codigo_item": CODITEM,
        "nombre_item": nombreItem,
        "saldo": SALDO1,
        "codigo_locacion": codigolocalicacion,
        "fecha_fifo": FECHAFIFO1,
        "fecha_exiracion": FECHAEXP,
        "numero_lote": NumeroLote,
        "HU_ID": Huid,
        "atributo_2": atributo2,
        "atributo_6": atributo2,
        "familia": familia,
        "fecha_stock": fechaIngreso
    }
    data= pd.DataFrame(data=format_json)
    json_data=data.to_json(orient='records')
    x=json.loads(json_data)
    info={}
    info['objects']=[]
    for y in x:
        info['objects'].append(y)
    with open('output/variables.json', 'w') as outfile:
            json.dump(info, outfile)
    #print(json_data)
# getJSONxDataFrame(path)
