import mysql.connector
from os import path, makedirs
import shutil

diract = path.dirname(path.abspath(__file__)) #Directorio donde se encuentra el script
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="zambospic"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM galeria")
myresult = mycursor.fetchall()

"""
1 = Recuerdo
2 = Comida
3 = Creatividad
4 = Paisaje
"""

# Creacion de Directorios para clasificacion
categos = {'recuerdo':diract+"/RECUERDO", 'comida' :diract+"/COMIDA", 'creatividad' : diract+"/CREATIVIDAD", "paisaje" : diract+"/PAISAJE"}
for tipo, dir in categos.items():
    if not path.exists(dir):
        makedirs(dir)

#Recorremos DB y clasificamos cada imagen
for x in myresult:
    s = list(x)
    categoria = s[1]
    imagen = s[3].replace('assets/galeria/', diract+'/galeria/')
    if path.exists(imagen) == True:  #Categorizamos solo si el archivo existe
        #print("File exists:",imagen) 
        if categoria == 1: 
            shutil.move(imagen,categos["recuerdo"])
        elif categoria == 2: 
            shutil.move(imagen,categos["comida"])
        elif categoria == 3: 
            shutil.move(imagen,categos["creatividad"])
        elif categoria == 4: 
            shutil.move(imagen,categos["paisaje"])
        else: print("Error con la imagen ",imagen, "No tiene una categoria")