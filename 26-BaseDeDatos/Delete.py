#######################################
#       Fichero: Delete.py            #
#     Elimina registros de las        #
#     tablas de base de datos         #
#######################################

# Importa la librería para utilizar SQLite
import sqlite3

# Conecta a la base de datos
database = sqlite3.connect('coches.db')

# Apertuda de un cursor
cursor = database.cursor()

# Lectura de todos los coches
cursor.execute("SELECT * FROM Coche")
print("Mostrando todos los coches:")
for registro in cursor:
    print(registro)

# Eliminación de un coche
query = "DELETE FROM Coche WHERE id = 3"
cursor.execute(query)
database.commit()

# Lectura de todos los coches
cursor.execute("SELECT * FROM Coche")
print("Mostrando todos los coches:")
for registro in cursor:
    print(registro)

# Cierra la conexión a la base de datos    
database.close()
