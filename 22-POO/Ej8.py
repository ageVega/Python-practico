class Coordenada:
    def __init__ (self, x, y):
        self.__X = x
        self.__Y = y
    def __GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X = x
    def SetY(self,y):
        self.__Y = y
coordenada = Coordenada(3,4)
print("(",coordenada.__GetX(),",",coordenada.GetY(),")")
