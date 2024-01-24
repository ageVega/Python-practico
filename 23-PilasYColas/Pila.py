class Pila:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def Apilar(self, item):
        self.__items.append(item)

    def Retirar(self):
        return self.__items.pop()

    def LeerCima(self):
        return self.__items[len(self.__items)-1]

    def NumeroElementos(self):
        return len(self.__items)

    def MostrarPila(self):
        print("Pila: ", self.__items,"<-- CIMA")

def SimuladorPila():
    fin = False
    pila = Pila()
    while not(fin):
        opc = input("Opcion:")
        if (opc=='1'):
            item = input("Introduzca elemento a apilar: ")
            pila.Apilar(item)
            print("Elemento apilado: ",item)
        elif(opc=='2'):
            if pila.EstaVacia():
                print("La pila está vacía, no puede retirarse ningún elemento")
            else:
                item = pila.LeerCima()
                pila.Retirar()
                print("Elemento retirado: ",item)
        elif(opc=='3'):
            if pila.EstaVacia():
                print("La pila está vacía, no puede leerse la cima")
            else:
                print("La cima es: ", pila.LeerCima())
        elif(opc=='4'):
            print("La pila tiene ",pila.NumeroElementos(), " elementos")
        elif(opc=='5'):
            if pila.EstaVacia():
                print("La pila está vacía")
            else:
                print("La pila no está vacía")
        elif(opc=='6'):
            pila.MostrarPila()
        elif(opc=='7'):
            fin = 1

print ("""*****************
Simulador de Pila
*****************
Menu
1) Apilar
2) Retirar
3) Leer cima
4) Número de elementos
5) ¿Está vacía?
6) Mostrar pila
7) Salir""")           
SimuladorPila()
