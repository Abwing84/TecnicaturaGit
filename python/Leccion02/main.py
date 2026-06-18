
"""# Class 06
# Sentencias de Control: if - else...//
condicion = 10
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion sin especificar")
# use modo debug...//"""
"""
"""
# Conversion de numero a texto...//
# num = int(input("Digite un numero en el rango del 1 al 3: "))
# numTexto = ''
# if num == 1:
#     numTexto = "Numero Uno"
# elif num == 2:
#     numTexto = "Numero Dos"
# elif num == 3:
#     numTexto = "Numero Dos"
# else:
#     numTexto = "Has ingresado un numero fuera de Rango"
# print(f'El numero ingresado es: {num} - {numTexto}')
# use modo debug ...//

# Operador Ternario: Sintaxis Simplificada...//
# condicion = False # Solo si el codigo es pequeño...//
# if condicion:
#     print("Condicion Verdadera")
# else:
#     print("Condicion Falsa")
# Sintaxis simplificada Operador Ternario
# print("Condicion Verdadera") if condicion else print("Condicion Falsa")

# Class 07 - Solo vamos a hacer ejercicios...//
# Ejercicio 3: Calcular estacion del año...//
"""mes = int(input('Digite un mes del año (1 - 12): '))
estacion = None # Variable vacia, en otyros lenguajes equivale a null...//

if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:
    estacion = 'Error, no hay numero para ese mes'

print(f'Para el mes {mes} la estacion es: {estacion}')
"""
# Ejercicio 4: Etapas de vida segun la edad...//
"""edad = int(input('Digite su edad: '))
mensaje = None

if 0 <= edad <= 10:  # Sintaxis simplificada
    mensaje = 'La infancia es increíble y bella'
elif 10 < edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'# Debes agregar para las demás edades
elif 30 <= edad < 50:
    mensaje = "La madurez llegó con la familia y las responsabilidades"
elif 50 >= edad < 100:
    mensaje = "Los nietos llegaron y con ellos otra vez las risas y los juegos"
else:
    mensaje = 'Error, etapa de vida no reconocida'

print(f'Tu edad es: {edad}, {mensaje}')
"""
# Ejercicio 5: Sistema de calificaciones...//
# El objetivo del programa sera crear un sistema de calificaciones de la siguiente manera:
# Le pedimos al usuario que ingrese un valor del 0 al 10.
# Luego si ingreso 9 o 10 = A
# Entre 8 y menor a 9 = B
# Entre 7 y menor a 8 = C
# Entre 6 y menor a 7 = D
# Entre 0 y menor a 6 = F
# De lo contrario el valor ingresado es incorrecto...//
"""
calificacion = int(input('Digite una calificacion entre 0 y 10: '))

if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion < 9:
    print('B')
elif 7 <= calificacion < 8:
    print('C')
elif 6 <= calificacion < 7:
    print('D')
elif 0 <= calificacion < 6:
    print('F')
else:
    print('Valor incorrecto...')
"""

















