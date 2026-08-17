
# Ejercicio 1: Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Definimos la tupla ...//
# Crear una lista que solo incluya los numeros 5 ...//
# e imprima por consola [1, 3, 2]

listas = [] # Definimos la listra...//
# Filtramos los elementos menores a 5 de la tupla...//
for elemento in tupla:
    if  elemento < 5:
        listas.append(elemento)
print(listas)

