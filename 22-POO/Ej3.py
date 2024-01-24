class Persona:
    def __init__ (self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))

print("OBJETOS ORIGINALES")
p1 = Persona("Alfredo","Moreno Muñoz", 35)
p1.MostrarPersona()
p2 = Persona("Valeria","Moreno", 1)
p2.MostrarPersona()
p1=p2
print("OBJETOS TRAS ASIGNACIÓN")
p1.MostrarPersona()
p2.MostrarPersona()
