class PersonaPublica:
    def __init__ (self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
    
class PersonaPrivada:
    def __init__ (self, nombre, apellidos, edad):
        self.__Nombre = nombre
        self.__Apellidos = apellidos
        self.__Edad = edad
    def GetNombre(self):
        return self.__Nombre
    def GetApellidos(self):
        return self.__Apellidos
    def GetEdad(self):
        return self.__Edad
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos
    def SetEdad(self, edad):
        self.__Edad = edad

publico = PersonaPublica("Alfredo","Moreno",35)
privado = PersonaPrivada("Valeria","Moreno",1)
print("PERSONA PÚBLICA")
print("Nombre: " + publico.Nombre)
print("Apellidos: " + publico.Apellidos)
print("Edad: " + str(publico.Edad))
print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))
print("\nModificación de valores en ambos objetos...")
publico.Apellidos = "Moreno Córcoles"
privado.SetApellidos("Moreno Muñoz")
print("PERSONA PÚBLICA")
print("Nombre: " + publico.Nombre)
print("Apellidos: " + publico.Apellidos)
print("Edad: " + str(publico.Edad))
print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))
