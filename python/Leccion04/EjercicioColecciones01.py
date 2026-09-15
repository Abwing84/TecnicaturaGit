# 4.1 clase 4 Python: Colecciones 1...//


# Ejercicio 1: Eliminar duplicados de una lista...//
# Escriuba un programa donde tenga una lista y que a continuacion...//
# elimine los elementos repoetidos, por ultimo mostrar la lista...//

# Creamos una lista...//
lista = [1, 2, 3, "Abel", 7, 7, 3, "Alberto", 1, "Abel", 2, "Alberto"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set...//
# lista = list(conjunto)
lista = list(set(lista)) # Convertimos la lista a conjunto y luego el conjunto a lista
# y lo guarda en la lista...// La conversion en una linea de codigo (eficiente)...//
print(lista)




