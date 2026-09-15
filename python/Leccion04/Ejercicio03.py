# 4.8 clase 4 Python: Colecciones: Insertar Elementos y Ordenarlos Función sort()...//
# Ejercicio 3: Insertar elementos y ordenarlos ...//
# Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0,
# nuestro programa dejaria de insertar. Por ultimo, mostrar los numeros ordenados de - a +...//
lista = []
salir = False
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else: lista.append(numero)
lista.sort() # La lista esta ordenada con esta funcion...//
print(f'\nlista ordenada: \n{lista}')
