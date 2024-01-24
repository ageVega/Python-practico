class Coordenada:
    def __init__ (self, x, y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X = x
    def SetY(self,y):
        self.__Y = y
        
class Cuadrado:
    def __init__ (self, v1,v2,v3,v4):
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4
    def __MostrarCoordenadaV1(self):
        print("(",self.__V1.GetX(),",",self.__V1.GetY(),")")
    def __MostrarCoordenadaV2(self):
        print("(",self.__V2.GetX(),",",self.__V2.GetY(),")")
    def __MostrarCoordenadaV3(self):
        print("(",self.__V3.GetX(),",",self.__V3.GetY(),")")
    def __MostrarCoordenadaV4(self):
        print("(",self.__V4.GetX(),",",self.__V4.GetY(),")")
    def MostrarVertices(self):
        print("El cuadrado está compuesto por los siguiente vértices:")
        self.__MostrarCoordenadaV1()
        self.__MostrarCoordenadaV2()
        self.__MostrarCoordenadaV3()
        self.__MostrarCoordenadaV4()

v1 = Coordenada(1,1)
v2 = Coordenada(4,1)
v3 = Coordenada(4,4)
v4 = Coordenada(1,4)
cuadrado = Cuadrado(v1,v2,v3,v4)
cuadrado.MostrarVertices()

