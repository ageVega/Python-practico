import Persona

class Alumno(Persona.Persona):
    def __init__ (self):
        self.__Curso = ""
        self.__Asignaturas = ""
    def GetCurso(self):
        return self.__Curso
    def SetCurso(self,curso):
        self.__Curso = curso
    def GetAsignaturas(self):
        return self.__Asignaturas
    def SetAsignaturas(self,asignaturas):
        self.__Asignaturas = asignaturas
    def MostrarAlumno(self):
        print("Alumno:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tCurso:",self.__Curso)
        print("\tMatrículas:",self.__Asignaturas)
