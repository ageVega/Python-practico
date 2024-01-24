def Sumar():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print ("La Suma es:", sum1+sum2)

def Restar():
    minuendo = int(input("Minuendo:"))
    sustraendo = int(input("Sustraendo:"))
    print ("La Resta es:", minuendo-sustraendo)

def Multiplicar():
    multiplicando = int(input("Multiplicando:"))
    multiplicador = int(input("Multiplicador:"))
    print ("La Multiplicacion es:", multiplicando*multiplicador)
    
def Dividir():
    try:
        dividendo = int(input("Dividendo:"))
        divisor = int(input("Divisor:"))
        print ("La Division es:", dividendo/divisor)
    except ZeroDivisionError:
        print ("ERROR: No se puede dividir por cero")

def Factorial():
    factorial = int(input("Introduzca el número del que quiere calcular el factorial: "))
    print("El factorial de " + str(factorial) + " es: " + str(FactorialCalculo(factorial)))

def FactorialCalculo(numero):
    if numero <=1:
        return 1
    else:
        return numero * FactorialCalculo(numero-1)

def Potencia():
    base = int(input("Introduzca la base de la potencia: "))
    exponente = int(input("Introduzca el exponente de la potencia: "))
    print("El valor de " + str(base) + " elevado a " + str(exponente) + " es: " + str(PotenciaCalculo(base,exponente))) 

def PotenciaCalculo(base,exponente):
    if exponente <= 0:
        return 1
    else:
        return base * PotenciaCalculo(base,exponente-1)
    
def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opcion:"))
        if (opc==1):
            Sumar()
        elif(opc==2):
            Restar()
        elif(opc==3):
            Multiplicar()
        elif(opc==4):
            Dividir()
        elif(opc==5):
            Factorial()
        elif(opc==6):
            Potencia()
        elif(opc==7):
            fin = 1

print ("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Factorial
6) Potencia
7) Salir""")           
Calculadora()
