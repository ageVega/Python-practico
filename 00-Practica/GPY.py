def contar_palabras(texto, palabra_a_buscar):
    # Convertir el texto y la palabra a buscar en minúsculas para hacer la búsqueda insensible a mayúsculas
    texto = texto.lower()
    palabra_a_buscar = palabra_a_buscar.lower()
    
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Contar las ocurrencias de la palabra
    contador = palabras.count(palabra_a_buscar)
    
    return contador

# Texto de ejemplo
texto = ("reacciones, cefuroxima se debe suspender inmediatamente y considerar un tratamiento alternativo. Si el paciente ha desarrollado una reacción grave como SSJ, NET o DRESS con el uso de cefuroxima, no se debe reiniciar el tratamiento con cefuroxima en este paciente en ningún momento. Reacción de Jarisch-Herxheimer Se ha observado la reacción de Jarisch-Herxheimer posteriormente al uso de cefuroxima (como axetilo) para el tratamiento de la enfermedad de Lyme. Ésta tiene lugar debido a la actividad bactericida de la cefuroxima (como axetilo) en el organismo causante de la enfermedad de Lyme, la espiroqueta Borrelia burgdorferi. Se debe tranquilizar a los pacientes de que esto es una consecuencia frecuente y generalmente autolimitante cuando se trata la enfermedad de Lyme con antibióticos (ver sección 4.8). Sobrecrecimiento de microorganismos no sensibles Como con otros antibióticos, el uso de cefuroxima (como axetilo) puede dar lugar a una sobreinfección producida por Candida. El uso prolongado también puede originar una sobreinfección producida por otros microorganismos no sensibles (p.ej. Enterococos y Clostridium difficile), que puede requerir la interrupción del tratamiento (ver sección 4.8). Se han comunicado casos de colitis pseudomembranosa asociados con casi todos los agentes antibacterianos, incluyendo la cefuroxima, y su gravedad puede oscilar de leve a mortal. Debe considerarse este diagnóstico en pacientes que desarrollen diarrea durante o después de la administración de cefuroxima (ver sección 4.8). Se debe considerar la interrupción del tratamiento con cefuroxima y la administración de un tratamiento específico para Clostridium difficile. No se deben administrar medicamentos que inhiben el peristaltismo (ver sección 4.8). Uso intracameral y trastornos oculares Cefuroxima no está formulado para uso intracameral. Se han notificado casos individuales y grupales de reacciones oculares graves después del uso intracameral, en viales de cefuroxima sódica autorizados para la administración intravenosa/intramuscular para los que el uso intracameral no estaba aprobado. Estas reacciones incluyeron edema macular, edema retiniano, desprendimiento de retina, toxicidad retiniana, alteraciones visuales, agudeza visual reducida, visión borrosa, opacidad corneal y edema corneal.")
contador = texto.lower().split().count('cefuroxima')
print(f"La palabra 'cefuroxima' se encuentra {contador} veces en el texto.")

palabra_a_buscar = "cefuroxima"

# Llamada a la función
contador = contar_palabras(texto, palabra_a_buscar)
print(f"La palabra '{palabra_a_buscar}' se encuentra {contador} veces en el texto.")

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
nombre_archivo = 'FichaTecnica.txt'  # Cambia esto por la ruta de tu archivo
palabra_a_buscar = 'cefuroxima'

# Llamada a la función y mostrar el resultado
contador = contar_palabras_en_archivo(nombre_archivo, palabra_a_buscar)
print(f"La palabra '{palabra_a_buscar}' se encuentra {contador} veces en el archivo.")
