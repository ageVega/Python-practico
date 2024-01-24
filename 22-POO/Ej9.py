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
    

class Alumno(Persona):
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

alumno = Alumno()
alumno.SetNombre("Alfredo")
alumno.SetApellidos("Moreno Muñoz")
alumno.SetEdad(35)
alumno.SetCurso("Bachillerato")
alumno.SetAsignaturas(["Matemáticas","Tecnología","Inglés"])
alumno.MostrarAlumno()
