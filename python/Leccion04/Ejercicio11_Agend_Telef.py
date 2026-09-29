# 6.2 Ejercicio 11 Agenda Telefónica...//
# Ejercicio 11: Agenda Telefonica...//
# Hacer un programa que simule una agenda de contctos. Crear un diccionario
# donde la clave sea el nombre del usuario y el valor sea el telefono, el
# programa tendra el siguiente menu de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir
agenda = {}
while True:
    print('\t...:MENU:...')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Ingrese su opcion: '))
    if opcion == 1:
        nombre = input('Digite nombre del contacto: ')
        telefono = input('Digite telefono del contacto: ')
        if nombre not in agenda:
            agenda [nombre] = telefono
            print('\nContacto agregado exitosamente')
        else:
            print('\nEste nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('\nSe ha eliminado el contacto requerido')
        else:
            print('\nEste contacto no existe en la agenda')
    elif opcion == 3:
        print('agenda de contactos')
        for claves, valor in agenda.items():
            print(f'Nombre: {claves}, Telefono: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break
    else:
        print('Se equivoco de opcion de menu')
    print()
