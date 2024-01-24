def Sumar(*valores):
    resultado = 0
    for item in valores:
        resultado = resultado + item
    return resultado

resultado = Sumar(3,87,45,63,345,3,58,33,22,11,99)
print("El resultado de la suma es: ", resultado)
