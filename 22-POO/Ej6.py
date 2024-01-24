class PersonaPrivada:
    def __init__ (self, nombre, apellidos, edad):
        self.__Nombre = nombre
        self.__Apellidos = apellidos
        self.__Edad = edad

privado = PersonaPrivada("Valeria","Moreno",1)
print("Nombre: " + privado.__Nombre)
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))
