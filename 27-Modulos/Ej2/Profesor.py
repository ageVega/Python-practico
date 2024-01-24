import Persona

class Profesor(Persona.Persona):
    def __init__ (self):
        self.__Antigüedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""
    def GetAntigüedad(self):
        return self.__Antigüedad
    def SetAntigüedad(self,antigüedad):
        self.__Curso = antigüedad
    def GetTutorias(self):
        return self.__Tutorias
    def SetTutorias(self,tutorias):
        self.__Tutorias = tutorias
    def GetTelefono(self):
        return self.__Telefono
    def SetTelefono(self,telefono):
        self.__Telefono = telefono
    def MostrarProfesor(self):
        print("Profesor:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tAntigüedad:",self.__Antigüedad)
        print("\tTutorias:",self.__Tutorias)
        print("\tTelefono:",self.__Telefono)

