# Clase 7: POO parte 3 Metodos SET & GET - tarea
# 10.1 Métodos: setter and getter parte 1 y 2...//

class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre}, {self._apellido}, {self._edad}')

# Metodo Getter, Necesita arriba del metodo un DECORADOR...//
    @property
    def nombre(self): # Metodo Getter...//
        print('Estamos usando el metodo get')
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

# Metodo Setter, tambien necesita el arriba del metodo el DECORADOR...//
    @nombre.setter
    def nombre(self, nombre):
        print('Estamos usando el metodo set')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self): # 10.6 Destructor de objetos
        print(f'Persona2: {self._nombre}, {self._apellido}, {self._edad}')
if __name__ == '__main__':
    persona1 = Persona2('Abel','Astudillo', 42)
    print(persona1.nombre) # Llamamos al metodo getter...//

    persona1.nombre = 'Juan Pedro' # Llamamos el metodo setter, Modifica el dato, asigna otro valor...
    print(persona1.nombre) # Otra vez con el metodo getter...//
    print(persona1.mostrar_detalle()) # Llamamos el metodo mostrar detalles...//

    # 10.2 Atributos read-only (solo lectura)
    #persona1._edad = 40 (no se puede hacer, es ignorancia sobre la sintaxis)
    #al borrar el metodo set y lo convierte en read-only...//
    #print(persona1.edad)

    # 10.3 Tarea: Con la clase Persona
    # Tarea:  hacer los ejercicios sin tener el video, estos ejercicios se los muestro después
    # de la entrega de la tarea, se debe enviar el enlace desde el repositorio de Github, es un
    # trabajo grupal, si se entrega antes de las 23 horas y los ejercicios estan bien resueltos,
    # tendrán la mejor nota, después de las 23 horas la nota baja, aprueban con 7.

    #Metodo getter y setter agregados
    # Objeto 1 de la tarea...
    persona2 = Persona2('Luis', 'Romero', 50)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Luis Sebastian'
    persona2.apellido = 'Romero Salinas'
    persona2.edad = 52
    print(persona2.mostrar_detalle())

    # Objeto 2 de la tarea...
    persona3 = Persona2('Anabela', 'Dominguez', 38)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Betiana'
    persona3.apellido = 'Lucero'
    persona3.edad = 36
    print(persona3.mostrar_detalle())

    # Objeto 2 de la tarea...
    persona4 = Persona2('Rambo', 'Apple', 7)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Rambo A.'
    persona4.apellido = 'Apple Holland'
    persona4.edad = 8
    print(persona4.mostrar_detalle())

    print(__name__)