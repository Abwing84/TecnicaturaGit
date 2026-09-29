# Leccion05 : Vi que el profe comiteo por eso es asi: leccion 05...//
# 6.3 clase 5 Python: List Unpacking: Desempaquetado de listas
# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Abel", "Astudillo"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion...//
show(*person) # Esto igual a lo anterior, pero ahora le pasamos todo junto...//
person2 = ("Mia", "Astudillo") # Desempaquetamos a traves de una tupla...//
show(*person2)
person3 = {"lastName": "Astudillo", "name": "Adriana"} # Desempaquetamos a traves de diccionario...//
show(**person3)

# 6.4 Repaso del Ciclo for else...//
numbers = [1, 2, 3, 4, 5] # aunque la lista este vacia se va ejecutar el else...//
for n in numbers:
    print(n)
#   if n == 3:
#        break # Unica manera para que no se muestre el else...//
else:
    print('Esto se termino')

# 6.5 List Comprehension: Lista de Comprensión...//
# list comprehension, lista de comprension...//
names = ["Abel", "Mia", "Candela", "Rambo"]
alongP = [a for a in names if a[0] == 'M'] # Esto regresa una nueva lista...//
print(alongP)

# Lista de comprension de diccionario...//
bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# 6.6 Funciones: Paso de Argumentos (funciones)...//
def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a traves del canal de YouTube")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Mia', 'Astudillo')
mi_funcion2('Cande', 'Astudillo')
mi_funcion2('Adri', 'Astudillo')

# 6.7 Funciones: Palabra return
# Creamos una funcion para sumar...//
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

# 6.8 Funciones: Valores por Default en Argumentos...//
def sumar2(a = 0, b = 0) : # Le damos un valor por default...//
    return a + b
resultado = sumar2()
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar2(22, 66)}')

# 6.9 Funciones: Argumentos, Variables en Funciones...//
def listarNombres(*nombres): # Normalmente se utiliza: *args...//
    for nombre in nombres: # Se va a convertir en Tuplas...//
        print(nombre)
listarNombres('Omar', 'Mariano', 'Sebastian', 'Maxi', 'Cristian')
listarNombres('Mia', 'Adriana', 'Candela', 'Italia', 'Mariano')
# No se pueden modificar por eso se van agregando(tuplas)...//
