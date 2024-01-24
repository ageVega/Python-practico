import statistics
print("La media de 5,3,7,9,4,2,2 es: ", statistics.mean([5,3,7,9,4,2,2]))
print("La mediana de 5,3,7,9,4,2 es: ", statistics.median([5,3,7,9,4,2]))
print("La mediana inferior de 5,3,7,9,4,2 es: ", statistics.median_low([5,3,7,9,4,2]))
print("La mediana superior de 5,3,7,9,4,2 es: ", statistics.median_high([5,3,7,9,4,2]))
print("La moda de 5,3,7,9,4,2,2 es: ", statistics.mode([5,3,7,9,4,2,2]))
print("La varianza de 5,3,7,9,4,2,2 es: ", statistics.variance([5,3,7,9,4,2,2]))
