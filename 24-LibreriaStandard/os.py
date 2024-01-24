import os
print("Directorio de trabajo actual: ",os.getcwd())
os.chdir("/Users/alfre/Desktop/")
print("Nuevo directorio de trabajo: ",os.getcwd())
print("ID del proceso: ", os.getpid())
print("ID del usuario del proceso: ", os.getuid())
