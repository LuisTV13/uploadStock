import os 
from os.path import isfile,join
from datetime import date, datetime
from utils.cred import getCred
from utils.getarchivos import getArchivos
from utils.getDataframe import getJSONxDataFrame
from utils.upHasura import insert_stock
import json

#Obteniendo Lista de Archivos
Corporativo = 'BDF'
ruta ='adjunto/'
contenido = os.listdir(ruta)
archivos = [nombre for nombre in contenido if isfile(join(ruta,nombre))]
x = len(archivos)
#obteniendo Fecha Actual
fecha=datetime.today().strftime('%d.%m.%Y')
date= '12.11.2021'
#obteniendo credenciales
correo,password = getCred(Corporativo)
#QUERY HASURA
query = """
mutation stock($objects: [StockAlmacenes_insert_input!]!) {
  insert_StockAlmacenes(objects: $objects, on_conflict: {constraint:StockAlmacenes_pkey}) {
    returning {
      codigo_item
    }
  }
}



"""
#LEER  JSON
archivo = open('output/variables.json')
variables = json.load(archivo)

#DESCARGAMOS LOS  ARCHIVOS
getArchivos(correo,password)
for i in range(0,x):
    pregunta = str(archivos[i])
    #print(pregunta.find(str(date)))
    if pregunta.find(str(fecha)) == 29:
        excel = ruta+pregunta
        print("SE ENCONTRO ARCHIVO CON FECHA  "+fecha)
        getJSONxDataFrame(str(excel))
        insert_stock(query,variables)
    else:
        print('NO')

