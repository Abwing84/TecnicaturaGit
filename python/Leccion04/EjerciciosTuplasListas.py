import math # Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)...//

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
# ------------------------------------------------------------------------- ...//

# 4.4 clase 4 Python: Colecciones: Ejercicio 1 con matematicas y la clase math...//
# Ejercicio de matematicas...//
# Para sacar la raiz cuadrada de un numero positivo...//
numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')

