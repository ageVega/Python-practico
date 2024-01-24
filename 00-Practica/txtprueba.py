def contar_palabras_en_archivo(nombre_archivo, palabra_a_buscar):
    try:
        # Abrir archivo en modo de lectura
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()
            
            # Convertir el contenido y la palabra a buscar en minúsculas
            contenido = contenido.lower()
            palabra_a_buscar = palabra_a_buscar.lower()
            
            # Dividir el contenido en palabras y contar
            contador = contenido.split().count(palabra_a_buscar)
        
        return contador
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return 0
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return 0

# Nombre del archivo y palabra a buscar
nombre_archivo = '../01-Files/texto.txt'  # Ruta relativa al archivo
palabra_a_buscar = 'cefuroxima'

# Llamada a la función y mostrar el resultado
contador = contar_palabras_en_archivo(nombre_archivo, palabra_a_buscar)
print(f"La palabra '{palabra_a_buscar}' se encuentra {contador} veces en el archivo.")
