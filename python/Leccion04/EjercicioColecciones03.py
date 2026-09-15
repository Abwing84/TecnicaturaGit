# 4.3 clase 4 Python: Colecciones 3...//


# Ejercicio 3: Agregar personajes a una lista...//
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos...//
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos una lista vacia...//
# Creamos diccionarios...//
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del norte'}
personajes.append(P) # Agregamos a la lista un personaje...//
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': "Gimli", 'Clase': "Guerrero", 'Raza': "Enano"}
personajes.append(P)
P = {'Nombre': "Frodo", 'Clase': "Portador", 'Raza': "Hobbit"}
personajes.append(P)
P = {'Nombre': "Boromir", 'Clase': "Guerrero", 'Raza': "Hombre"}
personajes.append(P) # Reutilizamos la variable P...//
print(personajes) 