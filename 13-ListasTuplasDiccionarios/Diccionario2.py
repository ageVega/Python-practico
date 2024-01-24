diassemanaingles = {"Lunes" : "Monday",
                   "Martes" : "Tuesday",
                   "Miercoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes" : "Friday"}
print(diassemanaingles)
diassemanaingles["Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)
