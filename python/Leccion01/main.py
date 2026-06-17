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

# 