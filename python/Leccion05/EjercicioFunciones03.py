# 7.5 Resultado de la tarea anterior, Ejercicio 3 (hacer tarea)...//
# Ejercicio 3: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#  Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debve imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el numero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan numeros negativos o 0 no imprime nada...//
def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base...//
        print(numero)
        imprimir_numeros_recursivos(numero - 1) # Caso Recursivo...//
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

imprimir_numeros_recursivos(5)
# Tarea que el usuario ingrese el numero...//
def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base...//
        print(numero)
        imprimir_numeros_recursivos(numero - 1) # Caso Recursivo...//
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

numeroRecursivo = int(input('Digite el numero para mostrar recursividad: '))
imprimir_numeros_recursivos(numeroRecursivo)