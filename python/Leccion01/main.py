''' #Doc string...//
# Class01...//
print("Hola Mundo desde Python")
# Class02...//
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#las literales se escriben de la siguiente manera:
# la variable x240
# la variable y984
# la variable z304
print(id(y))
print(id(z))
#a = False #10.78 # :str "es una referencia"...//
#print(type(a)) #COMO TYPE OF EN JAVASCRIPT, funcion que te puestra la class...//

# Class03...//
#Tipos int, float, String, Bool

x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejos de Cadenas (String)...//

miGrupoFavorito = "Divididos"
caractericas = "La Aplanadora del Rock"
print("Mi grupo favorito es: ", miGrupoFavorito, caractericas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos Booleanos (Bool)...//
mibooleano = 3 > 2
print(mibooleano)

if mibooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario ...//
# Funcion input ...//
resultado= input("Digite un numero: ") # Regresa un dato tipo  String...//
print(resultado)

# Conversion de la entrada de datos... en la funcion input...///
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# Ejercicio 1: Califica tu día
# ¿Cómo estuvo tu día (1 al 10)?
# Mi día estuvo de: 10
# Hacer el código
# Debes hacerlo en PyCharm y también en el celular y en la terminal de Python...

# Pedimos al usuario que ingrese un numero...//
calificacion = int(input("¿Como estuvo tu dia (Del 1 al 10)?"))
print("Mi dia estuvo de:", calificacion)

# Ejercicio 2:
# Se solicita incluir la siguiente información acerca de un libro:
# Título
# autor
# Debes imprimir la información en el siguiente formato:
# Proporciona el título:
# Proporciona el autor:
# <título> fue escrito por <autor>

# Pedimos los datos al usuario...//
titulo = input("Proporciona el título: ")
autor = input("Proporciona el autor: ")

# Mostramos la información en el formato solicitado...//
print(titulo, "fue escrito por", autor)
''' #DOCSTRING = CADENA PARA DOCUMENTAR...//
# Class04
## Operadores Aritmeticos...//
"""#Doc string...//
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma", suma)
print(f"Resultado de la suma es: {suma}")# Interpolacion, incluir variable en string...//

resta = operandoA - operandoB
print(f"Resultado de la resta es : {resta}")

multiplicacion = operandoA * operandoB
print(f"Resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"Resultado de la division es: {division}")
division = operandoA // operandoB
print(f"Resultado de la division (int) es: {division}")

modulo = operandoA % operandoB # modulo o residuo...//
print(f"Resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"Resultado de la exponente es: {exponente}") # DOC STRING = CADENA PARA DOCUMENTAR...//
''' # Ejercicio: Calcular el Area y Perimetro de un Rectangulo...//
# Proporciona el alto del rectángulo: 5
# Proporciona el ancho del rectángulo: 3
# Área: 15
# Perímetro: 16
# Las fórmulas para calcular el área y el perímetro de un rectángulo son:
# Área: alto * ancho
# Perímetro: (alto + ancho) * 2

alto = int(input("Proporciona el alto de un rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area: ", area)
print("Perimetro: ", perimetro)
""" #docstring, documnetacion formal...//
"""
#Operadores de asignacion y comparacion...///
miVariable3 = 10
print(miVariable3)

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 -= miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparacion...//

d = 4
b = 2
resultado = d == b # Comprobamos si son iguales
print(resultado)

# Operador Diferente...//
resultado = d != b
print(resultado)

# Operador mayor que...//
resultado = d > b
print(resultado)

# Operador menor que...//
resultado = d < b
print(resultado)

# Operador menor o igual que...//
resultado = d <= b
print(resultado)

# Operador mayor o igual que...//
resultado = d >= b
print(resultado)
"""
# Ejercicio 1: Numero par o impar...//
# 1. Solicitamos que el usuario ingrese un numero
# 2. Este se asigna a una variable...//
# 3. Utilizaremos la estructura 'if-else'
# 4. La formula: <num> % 2 == 0 Esta operacion nos
# dice si es numero par
# 5. Si es True imprimimos que es par
# 6. Si es False imprimimos que es impar
# Hacerlo en Pycharm...//
"""
a = int(input("Digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero Par")
else:
    print(f"El valor de a es: {a} es un numero Impar")
"""
"""
# Ejercicio 2: Determinar si es mayor de edad...//
# 1. Solicitamos que el usuario ingrese un numero
# 2. Alamacenar en una variable...//
# 3. Utilizaremos la estructura 'if-else'
# 4. La formula: <num> % >= 8
# 5. True imprimimos "Eres mayor de edad"
# 6. False imprimimos "Eres menor de edad"
# Hacerlo en Pycharm...//

edadAdulto = 18
edadPersona =int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")
"""
#Class 05
# Operadores Logicos...//
"""
# Operador and...//
a = True
b = True
resultado = a and b
print(resultado)
# Operador or...//
resultado = a or b
print(resultado)

# Operador not...// unario
resultado = not a
print(resultado)
"""
"""
# Ejercicio: Valor dentro del rango...//
# 1. Pedimos al usuario un valor.
# 2. Verificar si el valor se encuentra entre rango 0 a 5.
# 3. La formula es: <num> >= 0 and <num> <= 5.
# Hacerlo en Pycharm...///

valor = int(input("Digite un numero dentro del rango 0 a 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")
"""
"""
# Ejercicio: Operador or, Operador not...//
# La pregunta es si un padre puede asistir al juego de su hijo.
# 1. Verificamos si tiene vacaciones.
# 2. Verificamos si tiene el dia libre.
# 3.Usar estructura if - else.
# 4. Imprimir.
# Hacerlo en Pycharm...//

vacaciones = True
diaDescanso = True
if not(vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistire al juego")
"""
"""
# Ejercicio: Rango entre las edades 20 y 30 años...//
# Observa el final: Sintaxis simplificada del Operador and *1...//
# 1. Preguntar la edad al usuario.
# 2. Si la edad esta dentro de los 20 o 30 años, esta dentro del rango.
# 3. Combinamos los operadores and y or para saber si el usuario esta dentro del rango.
# Hacerlo en Pycharm...//

edad = int(input("Digite su edad : "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)
# Sintaxis simplificada del Operador and *1...//
# if veinte or treinta:
if(20 <= edad < 30) or ( 30 <= edad < 40):# *1 simplifica el and...//
    print("Estas dentro del rango de los (20'0) a (30'0) años")
#    if veinte: #indentacion un tab, abajo en la identacion hay dos tab...//
#        print('Estas dentro del rango de los (20\'0) años')
#    elif treinta:
#        print("Estas dentro del rango de los (30'0) años")
#    else:
#        print('no estas dentro del rango')
else:
    print("No estas dentro del rango de los (20'0) a los (30'0) años ")
"""
"""
# Ejercicio: El mayor de dos numeros...//
# Solicita al usuario dos valores, determinar cual es el mayor.
# 1. Solicita al usuario dos valores
# numero1 (int)
# numero2 (int)
# Se debe imprimir el mayor
# (la salida debe ser)
# Digite el valor para el numero1
# Digite el valor para el numero2
# El numero mayor es: <numeroMayor>

numero1 = int(input("Digite un valor para el numero1: "))
numero2 = int(input("Digite un valor para el numero2: "))
# Utilizacion modo debug main...//
if numero1 > numero2:
    print("El numero1 es mayor")
else:
    print("El numero2 es mayor")
"""
# Ejercicio: Tienda de libros...//
# 1. Mostrar: Ingrese los siguientes datos del libro.
# 2. Digite el nombre del libro.
# 3. Digite el ID del libro.
# 4. Digite el precio del libro.
# 5. Indicar si el envio es gratuito(True/False)
# 6. Mostrar:
#       Nombre:
#       ID:
#       Precio:
#       Envio Gratuito:

print("Digite los siguientes Datos ")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el envio es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrectop, debe escribir True/False"
print(f'''
        Nombre: "{nombre}"
        ID: {id}
        Precio: ${precio}
        Envio Gratuito?: {envioGratuito}
        
''')

