import os
import shutil
print("¡Cambiando directorio de trabajo!")
os.chdir("/Users/alfre/Desktop/Ejercicio/")
print("Nuevo directorio de trabajo: ",os.getcwd())
print("Contenido del directorio: ", os.listdir())
print("¡Eliminando el directorio NuevoDirectorio!")
shutil.rmtree("NuevoDirectorio")
print("Contenido del directorio: ", os.listdir())
print("¡Borrando el fichero prueba.txt!")
os.remove("prueba.txt")
print("Contenido del directorio: ", os.listdir())
