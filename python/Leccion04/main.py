# 2° SEMESTRE - PYTHON...//
# LECCION04
# Colecciones: listas...//
# 1.listas: indices...//
# listas = Ariel, Liliana, Natalia, Osvaldo.
# Dentro de la lista pueden haber nombres y numeros, osea cualquier tipo de dato...//
# a cada elemento en la lista se le asigna un indice el primero seria 0 cero ...//
# teniendo en cuenta cada indice, nos va a permitir acceder, modificar y eliminar
# cualquier elemento de la lista...//

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel'] # se puede utilizar comillas ' ' o " "...//
print(nombres)
print(nombres[0]) # muestra por indice el 1er elemento...//
print(nombres[1]) # MUESTRA EL 2° ELEMENTO
print(nombres[3]) # muestra ultimo elemento cuando conocemos la cantidad...//
print(nombres[-1]) # cuando la lista es muy larga, no conocemos la cantidad
# Se utiliza el indice -1...//
print(nombres[-2]) # manera inversa de recorrer las lista con los indices negativos...//

# 2.listas: recuperar rango de una lista...//
print(nombres)
print(nombres[0:2]) # va recorrer el indice 0 y 1, no el indice 2...//

# Ir del inicio de la lista al indice sin incluirlo el 0...//
print(nombres[ :3]) # dejamos vacio y el compilador entiende que es del indice 0 en adelante...//

# Ahora desde el indice indicado al final ...//
print(nombres[1: ])

# Modificar un valor en la lista...//
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista...//
for nombre in nombres: # muestra nombre por nombre, nombre es singular, la lista es plural...//
    print(nombre)
else:
    print('se acabaron los nombres de la lista')

# 3.listas: vamos a ver cuantos elementos tiene una lista...//
print (len(nombres)) # le pasamos como parametro la lista...//

# Agregamos un elemnto en la lista...//
nombres.append('Marcelo') # agrega el elemento al inicio o final de la lista...//
print(nombres) # lo hace al final, efecto "cola"...//

# Insertar un elemento en un indice especifico...//
nombres.insert(1,'Alberto')
print(nombres) # se desplaza el resto de la lista...//
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento de la lista...//
nombres.remove('Alberto')
print(nombres)
nombres.pop() # borra el ultimo elemento de la lista...//
print(nombres)

# Eliminamos un indice especifico...//
del nombres[2] # del significa delete (eliminar)...//
print(nombres)

# Eliminar, borrar o limpiar todos los elementos...//
nombres.clear()
print(nombres)

# Eliminar la lista...//
# del nombres # eliminar la lista por ese da ese error...//
# print(nombres) #  File "C:\Users\Abel\TecnicaturaGit\python\Leccion04\main.py", line 69, in <module>
#    print(nombres)
#          ^^^^^^^
# NameError: name 'nombres' is not defined. Did you mean: 'nombre'?

'''
sintaxis de range(inicio<opcional>, fin <requerido>, incremento <opcional>)

Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
Ejemplo de ejecución: 3,5,7,9
'''
# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
# Ejemplo de ejecucion: 0,3,6,9
# numeros = ['0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10']
print('Rango de 0 a 10 con números divisibles entre 3')
for i in range(11): # se pone 11 uno mas para que tome al 10...//
    if i % 3 ==0:
        print(i)

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimelos
# Ejemplo de ejecucion: 2,3,4,5,6
print('Rango con valores de inicio = 2 y fin = 6')
for i in range(2,7): # COMO LO HICE YO...//
    print(i)

print()

rango = range(2,7)
for i in rango:
    print(i)

# Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
for i in range(3,11,2):
        print(i)

print()

rango = range(3,11,2)
for i in rango:
    print(i)
# las listas son modificables o mutables...//
# funciones que usamos: append, insert, remove, pop, clear, del ...//

print()

# # Colecciones: tuplas...//
# 1.Tuplas: la tupla tiene ('agsdh',) no puede faltar la comilla y la coma sino lo toma como string...//
# Definimos una tupla...//
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis...//
print(cocina[0])

# Mostrar de manera inversa...//
print(cocina[-1])

# Como acceder a un rango...//
print(cocina[0:2]) # va a mostras un lugar como si hubiesemos puesto [0]...//

print()
# Ejemplo:
verduras = ('papa') # una tupla necesita aunque sea de un elemento " la , "(coma)...//
# de lo contrario seria un tipo str cadena

# 2.tuplas
# Recorremos los elementos de una tupla...//
for cocinar in cocina:
    print(cocinar, end=' ') # Print esta usando el backslash \n para saltos de linea
# entonces si agregamos , end=' ' para eliminar el salto de linea...//

# cocina[0] = 'plato'
# print(cocina) # muestra error porque no se puede agregar elementos en una tupa...//

# Como modificar una tupla a lista se modifica y luego se convierte de lista a tupla...//
# AUNQUE NO ES UNA BUENA PRACTICA, a menos que sea necesario...//

cocinalista = list(cocina)
cocinalista[0] = 'plato'
cocina = tuple(cocinalista)
print("\n", cocina)

# EN TUPLAS las funciones appent, insert, remove NO SE PUEDEN UTILIZAR
# del cocina esto es para eliminar una tupla
# print(cocina)

# Ejercicio 1: Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Definimos la tupla ...//
# Crear una lista que solo incluya los numeros 5 ...//
# e imprima por consola [1, 3, 2]


