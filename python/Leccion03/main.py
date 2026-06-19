
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
# Class 08
# Ejercicios y mucha practica...//
# Ejercicio: Año bisiesto...//
"""while True:
    # Ingreso del año
    anio = int(input("Ingrese un año: "))

    # Validación simple
    if anio < 0:
        print("Año inválido")
        continue

    # Condición de año bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

    # Opción para continuar (como en el diagrama)
    opcion = int(input("Para continuar digite 1, otro número para salir: "))

    if opcion != 1:
        print("Fin del programa")
        break
"""
# Ejercicio: Calcule un programa que ingrese N numero y calcule la suma...//
"""n = int(input("Ingrese un número: "))
suma = 0

while n > 0:
    suma += n
    n -= 1

print("La suma es:", suma)
"""
# Ejercicio: Ingrese 10 calcule cuales son positivos, negativos y neutros...//
"""conteoPositivos = 0
conteoNegativos = 0
conteoNeutros = 0

for i in range(1, 11):
    num = int(input(f"Ingrese el número {i}: "))

    if num > 1000000:
        print("Número invalido")
        continue

    if num > 0:
        conteoPositivos += 1
    elif num < 0:
        conteoNegativos += 1
    else:
        conteoNeutros += 1

print("Positivos:", conteoPositivos)
print("Negativos:", conteoNegativos)
print("Neutros:", conteoNeutros)
"""
# Ejercicio: Suponga que se tiene un conjunto de calificaciones de un grupo de
# 10 alumnos. Realizar un algoritmo para calcular la calificación promedio y la
# calificación más baja del grupo...//
"""suma = 0
calificacionBaja = 9999
i = 1
while True:
    if i > 10:
        break  # se repite 10 veces

    calificacion = float(input(f"Ingrese la calificación {i}: "))

    # Validación
    if calificacion < 0 or calificacion > 10:
        print("Calificación inválida")
        continue

    # Suma acumulada
    suma += calificacion

    # Buscar la menor calificación
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
    i += 1

# Promedio
calificacionPromedio = suma / 10

print("La calificación promedio es:", calificacionPromedio)
print("La calificación más baja es:", calificacionBaja)
"""

# Class 09
# Ejercicios 5: Calcula el factorial de un numero >= 0...//
"""num = int(input("Digite un número mayor o igual a 0: "))

if num < 0:
    print("Error, el número debe ser mayor o igual a 0")
else:
    i = 1
    factorial = 1

    while i <= num:
        # Ejemplo de uso de continue: saltar el 0 (aunque no afecta el factorial)
        if i == 0:
            i += 1
            continue

        factorial *= i
        i += 1

    print(f"El factorial de {num} es: {factorial}")
"""

# Ejercicio 6: Suma de pares, conteo de pares y promedio de impares...//

"""n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))

# Inicialización de variables
sumaPares = 0
conteoPares = 0
sumaImpares = 0
conteoImpares = 0

i = 1
while i <= n_elementos:
    num = int(input(f"Digite el número {i}: "))

    if num % 2 == 0:  # Número par
        sumaPares += num
        conteoPares += 1
    else:             # Número impar
        sumaImpares += num
        conteoImpares += 1

    i += 1

# Resultados finales
if conteoPares > 0:
    print(f"La suma de los números pares es: {sumaPares}")
    print(f"El conteo de los números pares es: {conteoPares}")
else:
    print("No se han digitado números pares")

if conteoImpares > 0:
    promedio_impares = sumaImpares / conteoImpares
    print(f"El promedio de los números impares es: {promedio_impares}")
else:
    print("No se han digitado números impares")
"""
# Ejercicio 7: Calcular salarios de 5 empleados y la sumatoria total...//
"""suma = 0  # acumulador de salarios

i = 1
while i <= 5:
    print(f"Salario del empleado {i}")
    horas = int(input("Digite las horas trabajadas: "))
    tarifa = float(input("Digite la tarifa por hora: "))

    salario = horas * tarifa
    print(f"El salario es: {salario}")

    suma += salario
    i += 1

print(print(f"La suma de todos los salarios es: {suma}"))
"""


