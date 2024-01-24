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

class Profesor(Persona):
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

alumno = Alumno()
alumno.SetNombre("Alfredo")
alumno.SetApellidos("Moreno Muñoz")
alumno.SetEdad(35)
alumno.SetCurso("Bachillerato")
alumno.SetAsignaturas(["Matemáticas","Tecnología","Inglés"])
alumno.MostrarAlumno()

profesor = Profesor()
profesor.SetNombre("Profesor")
profesor.SetApellidos("Casa Papel")
profesor.SetEdad(50)
profesor.SetAntigüedad(15)
profesor.SetTutorias([["Lunes","16-18"],["Jueves","12-14"],["Viernes","11-13"]])
profesor.SetTelefono("654321098")
profesor.MostrarProfesor()
