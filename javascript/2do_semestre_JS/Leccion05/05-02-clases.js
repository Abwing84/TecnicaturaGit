// Clase 6 : Creamos Leccion 05
// 6.1 Sintaxis de Clases en JavaScript: Parte 1 y 2
//let persona3 = new Persona('Carla', 'Ponce');
// No se puede crear alsar la clase para crear el objeto,
class Persona{// Clase padre...//6.4 Herencia: Parte 1 y 2
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
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
}
// 6.4 Herencia: Parte 1 y 2
class Empleado extends Persona(){// Clase hija...
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
}
// Creamos dos objetos...
let persona1 = new Persona('Martin', 'Diaz');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
perosona1.apellido = 'Araoz';// Tarea de video...//
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

// 6.4 Herencia: Parte 1 y 2 - Cree el diagrama UML... despues completar!!!

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);

