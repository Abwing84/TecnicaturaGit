# 7.7 Ejercicio 5 Funciones (Celsius a Fahrenheit)...//
# Ejercicio 5: Convertidor de temperaturas...//
# Realizar dos funciones para convertir
# de grados Celsius a Fahrenheit y viceversa
# Investigar las formulas...//

# Funcion Celsius a Fahrenheit
def celsius_fahreinhgeit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia: multiplicacion, division y suma...//

# Funcion Fahrenheit a Celsius
def fahreinhgeit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respeta la presedencia utilizando parentesis...//

celsius = float(input('Digite el valor de Celsius: '))
resultado = celsius_fahreinhgeit(celsius)
print(f'{celsius}°C a °F -> {resultado:.2f}°F')

fahrenheit = float(input('Digite el valor de Fahrenheit: '))
resultado = fahreinhgeit_celsius(fahrenheit)
print(f'{fahrenheit}°F a °C -> {resultado:.2f}°C')

