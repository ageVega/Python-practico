class Persona:
    def __init__ (self):
        self.__Nombre = "" 
        self.__Apellidos = ""
        self.__Edad = 0
    def GetNombre(self):
        return self.__Nombre
    def SetNombre(self,nombre):
        self.__Nombre = nombre
    def GetApellidos(self):
        return self.__Apellidos
    def SetApellidos(self,apellidos):
        self.__Apellidos = apellidos       
    def GetEdad(self):
        return self.__Edad
    def SetEdad(self,edad):
        self.__Edad = edad
