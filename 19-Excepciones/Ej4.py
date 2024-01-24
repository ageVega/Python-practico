print("¡Iniciando programa!")
print("\n¡Comenzando primera parte del programa!")
try:
    print(str(17/0))
except:
    print("ERROR: Division por cero")
else:
    print("INFO: no se han producido errores")
finally:
    print("¡Primera parte de programa acabada!")

print("\n¡Comenzando segunda parte del programa!")
try:
    print(str(17/1))
except:
    print("ERROR: Division por cero")
else:
    print("INFO: no se han producido errores")
finally:
    print("¡Segunda parte de programa acabada!")

