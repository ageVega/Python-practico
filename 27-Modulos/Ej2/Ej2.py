import Alumno
import Profesor

alumno = Alumno.Alumno()
alumno.SetNombre("Alfredo")
alumno.SetApellidos("Moreno Muñoz")
alumno.SetEdad(35)
alumno.SetCurso("Bachillerato")
alumno.SetAsignaturas(["Matemáticas","Tecnología","Inglés"])
alumno.MostrarAlumno()

profesor = Profesor.Profesor()
profesor.SetNombre("Profesor")
profesor.SetApellidos("Casa Papel")
profesor.SetEdad(50)
profesor.SetAntigüedad(15)
profesor.SetTutorias([["Lunes","16-18"],["Jueves","12-14"],["Viernes","11-13"]])
profesor.SetTelefono("654321098")
profesor.MostrarProfesor()
