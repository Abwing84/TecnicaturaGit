// Clase 6 : Creamos Leccion 05
// 6.1 Sintaxis de Clases en JavaScript: Parte 1 y 2
//let persona3 = new Persona('Carla', 'Ponce');
// No se puede crear alsar la clase para crear el objeto,
class Persona{// Clase padre...//6.4 Herencia: Parte 1 y 2

    static contadorPersona = 0;// 8.2 Atributos estáticos...//
    //email = 'Valor default email';// 8.3 Atributos No estáticos...//
    static get MAX_OBJ(){// 8.5 ESTE METODO SIMULA UNA CONSTANTE...//
        return 5;// Cantidad limite de creacion de objetos...//
    }

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersona < Persona.MAX_OBJ){// 8.5
            this.idPersona = ++Persona.contadorPersona;
        }
        else{// 8.5
            console.log('Se ha superado el maximo de objetos permitidos');
        }
        // 8.2 Atributos estáticos
        // Se pone el nombre de la clase para acceder al atributo static
        //this.idPersona = ++Persona.contadorPersona;// 8.4 Uso de la palabra static
        //console.log('Se incrementa contador: '+Persona.contadorObjetosPersona);
    }
// 6.2 Método Get y Set:

    get nombre(){
        return this._nombre;
    }  

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){// Tarea de video...//
        return this._apellido;
    }

    set apellido(apellido){// Tarea de video...//
        this._apellido = apellido;
    }

    nombreCompleto(){//7.1 Heredar
        return this.idPersona+' '+this._nombre+' '+this._apellido;// 8.4 Uso de la palabra static
    }
    // 7.3 Clase Object, toString, sobreeescribiendo el 
    // metodo de la clase padre object
    toString(){ // Regresa un string...//
        // se usa Polimorfismo. multiples formas en tiempo de ejecucion...//
        // Dependiendo si es una referencia de tipo padre o de tipo hija, 
        // se ejecutara el metodo de la clase padre o de la clase hija...//
        return  this.nombreCompleto();
    }

    static saludar(){// 8.1 Palabra static
        console.log('Saludos desde el metodo static');
    }

    static saludar2(persona){// 8.1 Palabra static
        console.log(persona.nombre+' '+persona.apellido);
    }
}
// 6.4 Herencia: Parte 1 y 2
class Empleado extends Persona{// Clase hija...
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    // Sobreescritura de metodos...// 7.2 Sobreescritura
    nombreCompleto(){ // 7.2 Sobreescritura
        //return this._nombre+' '+this._apellido+', '+this._departamento; NO ESTARIA CORRECTO...//
        return super.nombreCompleto()+', '+this._departamento;
    }


}
// Creamos dos objetos...
let persona1 = new Persona('Martin', 'Diaz');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
persona1.apellido = 'Araoz';// Tarea de video...//
console.log(persona1.nombre);
console.log(persona1.apellido);// Tarea de video...//
//console.log(persona1);
let persona2 = new Persona('Sebastian', 'Castillo');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
persona2.apellido = 'Castelli';// Tarea de video...//
console.log(persona2.nombre);
console.log(persona2.apellido);// Tarea de video...//
//console.log(persona2);

// 6.2 Método Get y Set: Parte Get y Parte Set...
// Trabaje en el bloque anterior desde linea 8 y modifiquye las salidas...//

// 6.3 hoisting y clases: Parte 1 y 2...// linea 3 y 4 ...//
// antes de la creacion de la clase no se puede crear una variable new Persona
// No se puede crear un oibjetos sin antes iniciar la clase que le 
// permite hacer la instancia...//
// En Javascript NO EXISTE el concepto de HOISTING...//

// 6.4 Herencia: Parte 1 y 2 - Cree el diagrama UML... 

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());//7.1 Heredar

// Clase 7-A: Clases Parte 2
// 7.1 Heredar métodos .... en clase hija...//

// 7.2 Sobreescritura de metodos...//
// Cree el index.html...//
// en clase hija se puede sobreescribir un metodo de la clase padre...//

// 7.3 Clase Object, toString, sobreescritura y Polimorfismo
// clase Empleado es hija de la clase Persona y la clase Persona es hija de la
// clase Objeto, hereda automaticamente y no es necesario colocar ?extends'...//
// La clase Object es la clase padre de todas las clases en JavaScript
// y la misma contiene a su vez varios metodos dentro de ella...//

// Metodo toString() de la clase Object, nos permite mostrar un objeto en forma 
// de cadena de texto(IMPRIME LOS VALORES ACTUALES DE LOS ATRIBUTOS DE CADA UNO 
// DE LOS OBJETOS)... ES BUENA PRACTICA...//
// Detalle: en la clase Object existen metodos directamente en la clase object 
// o metodos definidos en el atributo prototype...//

//Object.prototype.toString..., Esta es la forma de acceder a atributosd y 
// metodos de manera dinamica...//
console.log(empleado1.toString());
// Polimorfismo: al imprimir el nombre completo + el departamento, significa 
// que el mismo método toString() se comporta de manera diferente según el tipo 
// de objeto que lo llama. Porque departamento se agrego en la clase hija, y el 
// toString se coloco en la clase padre, y al llamar al metodo toString() se 
// comporta de manera diferente para la clase Persona y para la clase Empleado, 
// porque la clase Empleado es hija de la clase Persona y tiene un atributo 
// adicional llamado departamento...//
console.log(persona1.toString());
// ver lineas superiores linea 30 aprox. ...//

// Clase 7-B: Static... y metodos estaticos...//
// 8.1 Palabra static con métodos: Parte 1 y 2
//persona1.saludar(); // No se puede llamar a un metodo static desde un objeto,
// porque el metodo static pertenece a la clase y no a los objetos de la clase...//

Persona.saludar(); // Se puede llamar a un metodo static desde la clase, porque 
// el metodo static pertenece a la clase y no a los objetos de la clase...//   
Persona.saludar2(persona1); 
// Metodo estatico: No se púede ver en la visualizacion previa, Solo se puede 
// ver la salida desde la consola o el metodo static...//
//funciona de forma diferente, lo podemos hacer de la clase y no de los objetos...//
//parte 2 en linea 42 concatena persona.apellido...//
Empleado.saludar();
Empleado.saludar2(empleado1);

// 8.2 Atributos estáticos
// desde linea 6 7 8
//console.log(persona1.contadorObjetosPersona); // undefined, porque el atributo
console.log(Persona.contadorObjetosPersona); // 0, porque el atributo static 
// pertenece a la clase y no a los objetos de la clase...//
console.log(Empleado.contadorObjetosPersona); 
// Las clases hijas heredan los atributos static de la clase padre, por lo tanto
// se puede acceder al atributo static desde la clase hija...//

// 8.3 Atributos estáticos vs No estáticos...//
console.log(persona1.email); // Valor default email, porque el atributo email
console.log(empleado1.email); // Valor default email, porque el atributo email
//console.log(Persona.email); // undefined, porque el atributo email NO es static y pertenece a los objetos...//

// 8.4 Uso de la palabra static: Parte 1 y 2
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersona);

let persona3 = new Persona('Carla', 'Pertosi');
console.log(persona3.toString());
console.log(Persona.contadorPersona);

// 8.5 Creación de constantes estáticas...//
// Que pasa si quiero agregar una variable Estatica No modificable...//
console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; // No se puede modificar ni alterar...
console.log(Persona.MAX_OBJ);
let persona4 = new Persona('Franco', 'Colapinto');
console.log(persona4.toString());

let persona5 = new Persona('Sasha', 'Podka');
console.log(persona5.toString());
// No se pueden agregar mas objetos ...//