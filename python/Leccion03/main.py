
# Class 07
# Ciclo while, significa Mientras o Durante...//
"""contador = 0
while contador < 5:
    print("Ejecutamos nuestro ciclo while ", contador)
    contador += 1
else:
    print("Fin del ciclo while")
"""
# Ejercicio : Imprimir los numeros del 0 al 5 con el ciclo while...//
"""maximo = 5
contador = 0
while contador <= maximo:
    print("Numero: ", contador)
    contador += 1
# use debug main...//
"""
# Ejercicio: Imprimir los numeros de forma descendente...//
"""minimo = 0
contador = 5
while contador >= minimo:
    print("Numero: ", contador)
    contador -= 1
# use debug main...//
"""
# Ciclo for, ciclo para, iterar recorrer cada elemento de un conj de datos...//
"""cadena = "Hola amigos"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")
# use debug main...//
"""
# Palabra reservada break...//
# Encuentra las letra a en la palabra y se puede poner break que detiene ...//
"""for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break # rompe el ciclo y se detiene en ese punto...//
else:
    print("Fin del ciclo for")
    """

# Palabra reservada continue ...//
# Numerops pares que se encuentra en un rango de 0 a 6...//
"""for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}')
# uso de continue...//
for i in range(6):
    if i % 2 == 1:
        continue # elude los numeros impares...//
    print(f'Valor: {i}')
"""








