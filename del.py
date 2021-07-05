import pandas as pd
from os import path, makedirs, remove
import shutil

diract = path.dirname(path.abspath(__file__)) #Directorio donde se encuentra el script
dmt = diract+"/eliminadas"
if not path.exists(dmt):
    makedirs(dmt)
archivo = diract+r"\galeria.csv" # Nombre del Archivo CSV donde estan las imagenes
data = pd.read_csv(archivo,sep=';') 
cn=0
carpeta = diract+"/galeria" #Nombre de la carpeta donde estan las imagenes
for dato in data["nombre"]:
    imagen = carpeta+"/"+dato
    if path.exists(imagen) == True:  #Categorizamos solo si el archivo existe
        shutil.move(imagen,dmt) #Esta funcion solo lo mueve de carpeta
        #remove(imagen) #Esta es la funcion que elmina por completo el archivo del sistema
        cn+=1
        print("Imagen Removida: ",dato)
        
print("Proceso Finalizado, cantidad de imagenes eliminadas:",cn)