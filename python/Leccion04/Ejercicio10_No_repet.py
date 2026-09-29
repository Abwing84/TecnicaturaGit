# 6.1 Ejercicio 10 No Repetir Caracteres ...//
# Ejercicio 10: No repetir caracteres ...//
# Hacer un programa que pida una cadena por teclado, luego
# al meter los caracteres en una lista sin repetir caracteres...//

cadena = input("Introduce una cadena: ") # Ingreso la cadena...//
caracteres = [] # Creamos una lista vacia
for caracter in cadena:
    if caracter not in caracteres: # Si el caracter aun no esta en la lista...//
        caracteres.append(caracter) # Lo agregamos a la lista...//
print(f'\nlista de caracteres sin repetir ningun: \n {caracteres}')