
# Ejercicio 4: Area y longitud de un circulo...//
# Hacer un programa para ingresar el radio de un círculo y se reporte
# su area y la longitud de la circunferencia.
#               Area = Pi * r^2
#               Longitud = 2 * Pi * r
# En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi
# Se escribe: import math...//

import math

# Pedimos el radio al usuario...//
radio = float(input("Proporciona el radio del círculo: "))

# Calculamos area y longitud
area = math.pi * (radio ** 2)
longitud = 2 * math.pi * radio

# Mostramos resultados...//
print("Area =", area)
print("Longitud =", longitud)
