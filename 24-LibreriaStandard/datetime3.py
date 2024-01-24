import datetime
ahora = datetime.datetime.now()
fecha = datetime.datetime(2017,11,29,23,19,00,123)
print("Se va a realizar la resta de las siguientes fechas:")
print("1.- ", ahora)
print("2.- ", fecha)
resultado = ahora - fecha
print("Resultado: ",resultado)
