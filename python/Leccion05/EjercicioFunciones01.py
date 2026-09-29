# 6.9.1 Clase 5: Ejercicio Funciones 01
# Ejercicio 01: Crear una funcion para sumar los valores recibidos tipo
# numericos, utilizando argumentos variables *args como parametro de la
# Funcion agregar como resultado la suma de todos los valores pasados
# como argumento...//
# Definiendo una funcion...//
def sumar_valor(*args):  # Recibimos una cantidad de parametros indefinidos...//
    resultado = 0
    # Iterar cada elemento...//
    for valor in args:
        resultado += valor
    return resultado


# Llamamos a la funcion...//
print(sumar_valor(3, 5, 9, 2, 1))