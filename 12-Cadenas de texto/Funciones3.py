cadena = input("Introduzca una cadena:")
buscar = input("Introduzca una cadena para buscar:")
print("¿Comienza la cadena por la cadena a buscar? (startswith):",cadena.startswith(buscar))
print("¿Termina la cadena por la cadena a buscar? (endswith):",cadena.endswith(buscar))
print("¿Cuántas veces aparece la cadena a buscar en la cadena? (count):",cadena.count(buscar))