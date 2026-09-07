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

# Agregamos un elemento en la lista...//
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

# 2.1 Clase 2 Python: tipo set o conjunto...//
# Tipo set se utilizan llaves...//
planetas = {'Martes', 'Júpiter', 'Venus'} # set o conjunto No mantiene orden no tiene indice...//
print (len(planetas)) # Usamos la funcion len = length significa largo...//

# Revisar si un elemento existe dentro de set...//
print('Júpiter' not in planetas) # Esto es una pregunta 'in' or 'not int'...//

# Agregar un elemento...//
planetas.add('Tierra') # add es una funcion...//
planetas.add('Tierra')
planetas.add('Tierra') # No permite agregar elementos duplicados...//
print(planetas)

# Eliminar elementos, puede arrojar error si el elemento no existe...//
planetas.remove('Júpiter') # ingresa un error muestra 'key error'
print(planetas)

planetas.discard('Tierr') # esta funcion al equivocarse no muestra error,
# solo que no lo elimina...//
print(planetas)

# Limpiar set...//
planetas.clear()
print(planetas)

# Elimina set o conjunto...//
del planetas
#print(planetas) # al eliminar nos muestra error...//

# 2.2 Clase 2 Python: Diccionario en Python...//
# 'Maradona':10 // el conjunto de dos elementos, lo que va entre comillas y despues del punto
# hace el diccionario y se usa {llñaves}...//
# dict(key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario...///
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave (key)...//
print(diccionario['IDE'])

# Otra forma de recuperar un elemento...//
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar los elementos...//
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'# un diccionario puede modificarse...//
print(diccionario)

# Como recorrer los elementos...//
for termino in diccionario:
    print(termino) # solo muestra las llaves...//

# Necesitamos una funcion para recorrer un diccionario...//
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario...//
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves...//

# Usamos una funcion para acceder al valor...//
for valor in diccionario.values():
    print(valor)

# Comprobamos la existencia de algun elemento...//
    print('IDE' in diccionario) # devuelve un booleano...//

# Agregamos un elemento al diccionario...//
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento del diccionario...//
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario...//
diccionario.clear()
print(diccionario)

# Eliminar un diccionario...//
del diccionario # El diccionario se borro...//

# 2.3 Clase 2 Python: Repaso de las listas en Python...//
# Agregamos un elemento en la lista...//
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)

# Concatenar listas...//
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2 # concatenamos ...//
print(lista3)


lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista...//
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado...//
# print(lista3.index(0)) # esto daria error porque este elemento no esta en la lista...//

# Como saber cuantos valores repetidos hay dentro de una lista...//
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista...//

# Para poner al reves una lista...//
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos...//
lista = [1, 2, 3] * 2
print(lista)

# Metodos de ordenamiento...//
lista3.sort() # Ordena los elementos en forma ascendente...//
print(lista3)

lista3.sort(reverse=True) # Ordena en forma descendente...//
print(lista3)

# 2.4 Clase 2 Python: Repaso y mas concepto de Tuplas en Python...//
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener dif tipos de datos...//
print(tupla)

print(4 not in tupla) # Accion booleana, su respuesta es de tipo booleana...//
# Por lo que podemos usar dentro de tuplas: index, count, len...//
# En tuplas se puede convertir de tupla a lista y lista a tuplas...//

# 3.1 Clase 3 python: Repaso del tipo set o conjunto...//
# para definir un conjunto...//
conjunto2 = set()
conjunto1 = {'bye', } # estando vacio con llaves, esta inicializado vacio...//
conjunto2.add(7)
conjunto2.add('hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el 3 No esta en el conjunto1...//

# Como hacer la igualdad de dos conjuntos...//
print(conjunto1 == conjunto2) # Nos devuelve un booleano como respuesta...//

# operaciones de conjuntos...//
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjunto...//
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # que elemento tienen en comun...//
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor del conjunto 1 y no el conjunto2...//
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # ^ = alt+94 | elemento que no comparten o son diferentes...//
print(conjunto3)

conjunto3 = conjunto1 | conjunto2 # Abajo preguntamos si un conjunto esta dentro de otro...//
print(conjunto2.issubset(conjunto3)) # Porque lo unimos antes, entonces esta funcion te muestra el subconjunto...//
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Pregunta si estan todos los elementos del conjunto1 en el 3...//
print(conjunto3.issuperset(conjunto2)) # CONJUNTO3 ES UN SUPERCONJUNTO TIENJE EL DE 1 Y EL DE 2...//
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son desconexos, esto es No comparten elementos...//
print(conjunto1.isdisjoint(conjunto2)) # Pregunta: No hay cosas en comun...//

# Convertir un conjunto totalmente inmutable...//
conjunto1 = frozenset # Esto hace el conjunto inmutable...//
# No se puede agregar, modificar y/o eliminar elementos del conjunto...//

# 3.2 clase 3 Python: Repaso de Diccionarios...//
diccionarioNuevo = {'Azul': 'blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar...//
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Diccionarios pueden almacenar diferentes tipos de datos...//
diccionario2 = {'Abel': {'Edad': 42, 'Altura': 1.75}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

# 3.3 clase 3 Python: Ejercicio con Diccionario y tarea...//
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 39, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    22: {'Nombre': 'Lautaro Martinez', 'Edad': 29, 'Altura': 1.74, 'Precio': '38 Millones', 'Posicion': 'Centro Delantero'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 32, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media punta'},
     3: {'Nombre': 'Nicolas Tagliafico', 'Edad': 33, 'Altura': 1.72, 'Precio': '25 Millones', 'Posicion': 'Lateral Izquierdo'},
     6: {'Nombre': 'Lisandro Martinez', 'Edad': 28, 'Altura': 1.76, 'Precio': '30 Millones', 'Posicion': 'Defensor'},
     5: {'Nombre': 'Leandro Paredes', 'Edad': 32, 'Altura': 1.82, 'Precio': '38 Millones', 'Posicion': 'Mediocampista'},
     18: {'Nombre': 'Nicolas Paz', 'Edad': 21, 'Altura': 1.86, 'Precio': '27 Millones', 'Posicion': 'Mediocampista'},
     15: {'Nombre': 'Nicolas Gonzalez', 'Edad': 28, 'Altura': 1.81, 'Precio': '20 Millones', 'Posicion': 'Mediocampista'},
     1: {'Nombre': 'Emiliano Martinez', 'Edad': 34, 'Altura': 1.95, 'Precio': '32 Millones', 'Posicion': 'Arquero'}
}
print(seleccionArgentina.values()) # no se ingresa datos en el parentesis, solo muestra los valores...//
print(seleccionArgentina[5]) # Busca por llave y muestra los valores...//
print(seleccionArgentina)

for valor in seleccionArgentina.values(): # llaves tambien pero sin .values()...//
    print(valor)
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Tarea: Agregar 4 jugadores al diccionario seleccionArgentina...//
print('Tenemos cargados en el diccionario la cantidad de:', len(seleccionArgentina), 'jugadores')

# 3.4 clase 3 Python: Metodo con listas llamado PILAS...//
pila = [1, 2, 3] # Es una lista...//

# Agregamos elementos a la pila por el final...//
pila.append(4)
pila.append(5)
print(pila)

# Sacando elementos por el final...//
pila.pop() # Saca el ultimo elemento de la la pila,
print(pila)

elementoBorrado = pila.pop()
print(f'Sacamos el elemento de la lista: {elementoBorrado}')
print(f'La lista pila ahora quedo asi: {pila}')

# 3.5 clase 3 Python: Metodo con listas llamado COLAS...//
# Estructura de datos tipo fifo (first imput / first output)
cola = ['Abel', 'Mia', 'Cande', 'Betiana']

# Agregamos elementos al final de la cola...//
cola.append('Natalia')
cola.append('Italia')
cola.append('Adri')
cola.append('Anabel')
print(cola)

# Sacamos elementos en la cola...// por orden de atencion...//
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)


