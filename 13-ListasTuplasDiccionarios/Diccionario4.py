diassemanaingles = {"Lunes" : "Monday",
                   "Martes" : "Tuesday",
                   "Miercoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes" : "Friday"}
print("Diccionario original: ",diassemanaingles)
diccionariocopia = diassemanaingles.copy()
print("Diccionario copy: ",diccionariocopia)
print("Valor del Lunes (pop): ", diassemanaingles.pop("Lunes"))
print("Diccionario después del pop: ",diassemanaingles)
print("Elemento al azar con popitem: ", diassemanaingles.popitem())
print("Diccionario después del popitem: ",diassemanaingles)
print("Valor del Martes (get): ",diassemanaingles.get("Martes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ",diassemanaingles.get("Lunes","No existe"))
diassemanaingles.update({"Lunes":"MondayNUEVO","Martes":"TuesdayNUEVO"})
print("Diccionario después del update: ",diassemanaingles)
print("setdefault del Sábado: ",diassemanaingles.setdefault("Sabado","Saturday"))
print("Diccionario después del setdefault (nuevo elemento): ",diassemanaingles)
print("setdefault del Lunes: ",diassemanaingles.setdefault("Lunes","Lunes"))
print("Diccionario después del setdefault (elemento existente): ",diassemanaingles)
print("Elemento iterable (items): ",diassemanaingles.items())
print("Elemento iterable (claves): ",diassemanaingles.keys())
print("Elemento iterable (valores): ",diassemanaingles.values())
print("Diccionario después del clear: ",diassemanaingles.clear())
