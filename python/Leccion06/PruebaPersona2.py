# 10.4 Uso de clases y módulos
from Persona import Persona
from Persona2 import Persona2
print('Creacion de onjetos'.center(50,'-'))
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 39)
    persona5.mostrar_detalle()

    # 10.5 Comprobación del módulo principal en ejecución
    # Trabajamos clase Persona2....
    print(__name__)
# Comprobacion de metodo de ejecucion principal en ejecucion:
# Sirve para saber de donde se esta ejecutando nuestro codigo,
# cuando estamos creando nuevos tipos o nuevas funcviones
# y estamos haciendo pruebas en el mismo archivo, entonces
# conviene agregarla, asi cuando importemos los nuevos tipos
# el codigo de prueba no se va ejecutar...//

# 10.6 Destructor de objetos
print('Eliminacion de objetos'.center(50,'-'))
del persona5 # No es comun pero se utiliza...//
