//Clase 4: Objetos parte 1...//
//1.1 Introducción a los Objetos en JavaScript Parte 1 y 2
let x = 10;
console.log(x.length)
console.log('#Tipo primitivos');//1.6 agregado por el profesor...//
//Objetos
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 32,
    idioma: 'es', //  El idioma se maneja en MAYUS...//
    get lang(){
        return this.idioma.toUpperCase();// Convierte las minus a mayus...//
    },
    set lang(lang){
        this.idioma = lang.toUpperCase;
    },
    nombreCompleto: function(){ // 1.2 - Metodo o function en javascript
        return this.nombre+' '+this.apellido;
    } ,// this..... apunta a los atributos o metodos del objeto...//
    get nombreEdad(){ //5.1 Métodos get y set Parte 1 y 2
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }  
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
// 1.2 Agregamos métodos a los Objetos
console.log(persona.nombreCompleto());
console.log('#Ejecutando con un objeto');//1.6 agregado por el profesor...//

//1.3 Diferentes formas de crear un Objeto
let persona2 = new Object(); // Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 15';
persona2.telefono = '5492615486875';
console.log(persona2.telefono);
console.log('#Creamos un nuevo objeto');//1.6 agregado por el profesor...//
//1.4 Cómo acceder a las propiedades de los Objetos...//
console.log(persona['apellido']) // Accedemos como un arreglo
console.log('#Usamos el ciclo for in');//1.6 agregado por el profesor...//
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}// primero accedemos a la propiedad y luego al valor...//
console.log('#Cambiamos y eliminamos un error');//1.6 agregado por el profesor...//
//1.5 Agregar y eliminar propiedades de los Objetos...//
persona.apellida = 'Betancud'; // Cambiamos dianamicamente el valor del objeto...//
delete persona.apellida // Eliminamos la propiedad con error...//
console.log(persona);

//1.6 Ejecutamos desde el navegador...//
// Vamos al explorador de carpetas y creamos un archivo html (index.html)...//
// Se agrega console.log('titulos y/o acciones, para mejor orden en consola)...//

// 1.7 Distintas formas de imprimir un Objeto con: Object.values()  
// y JSON.stringify()
// Numero 1: la mas sencilla es concatenar cada valor de cada propiedad...//
console.log('Distintas formas de imprimir un Objeto: Forma 1');
console.log(persona.nombre+', '+persona.apellido);

// Numero 2: A traves del ciclo for in...//
console.log('Distintas formas de imprimir un Objeto: Forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

// Numero 3: Object.values()...//
console.log('Distintas formas de imprimir un Objeto: Forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Numero 4: utilizaremos el metodo JSON.stringify()...//
console.log('Distintas formas de imprimir un Objeto: Forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString); 
// se adecua al manejo de objetos en JavaScript y es muy utilizado en la actualidad...//

//1.8 Investigamos JSON con chatGPT y vemos el uso de stringify y parse...//
//
// Clase 5. Objetos parte 1... lo agrgo dentro del objeto en la linea 15...//
// 5.1 Métodos get y set Parte 1
console.log('Comenzamos a utilizar el Metodo get');
console.log(persona.nombreEdad);
// Parte 1 ..//
console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'EN';
console.log(persona.idioma); // Devuelve el idioma en mayusculas...//

// 5.2 Constructores de objetos
function Persona3(nombre, apellido, email){// Constructor...//
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){ // Metodo dentro del constructor...//
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';// Se puede modificar o preasignar en el constructor...//
padre.telefono = '5492622469452';// Se puede agregar un nuevo atributo al objeto...//5.5 El uso de prototype...
console.log(padre);
// Creamos otro objeto...//
let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
// la palabra reservada new nos esta asignando un espacio diferente de memoria
// cuando se modifica se afecta solo ese espacio nuevo que se creo y no altera 
// el resto...//

// 5.3 Agregar métodos al constructor del objeto...// en linea 100!
console.log(padre.nombreCompleto());
console.log(madre.telefono); // 5.5 El uso de prototype...//
console.log(madre.nombreCompleto()); 

// 5.4 Distintas formas de crear objetos...//
// Diferentes formas de crear Objetos...//
// Caso 1...
let miObjeto = new Object(); // 1. Forma formal de crear un objeto...//
// Caso 2...
let miObjeto2 = {}; // 2. Forma literal de crear un objeto...// 

// Caso String 1...
let miCadena1 = new String('Hola'); // 1. Forma formal de crear un objeto...//
// Caso String 2...
let miCadena2 = 'Hola'; // 2. Forma literal de crear un objeto...//

// Caso con numeros 1...
let miNumero = new Number(1); // 1. Forma formal, NO RECOMENDADA...//
// Caso con numeros 2...
let miNumero2 = 1; // 2. Forma literal, SINTAXIS RECOMENDADA...//

// Caso con booleanos 1...
let miBoolean = new Boolean(false); // 1. Forma formal de crear un objeto...//
// Caso con booleanos 2...
let miBoolean2 = false; // 2. Forma literal, SINTAXIS RECOMENDADA...//

// Caso con Arreglos 1...
let miArreglo = new Array(); // 1. Forma formal de crear un objeto...//
// Caso con Arreglos 2...
let miArreglo2 = []; // 2. Forma literal, SINTAXIS RECOMENDADA...//

// Caso con Funciones 1...
let miFuncion = new Function(); // 1. Forma formal, Todo despues de new es 
// considerado objeto...//

// Caso con Funciones 2...
let miFuncion2 = function(){}; // 2. Forma literal, Notacion simplificada
// SINTAXIS RECOMENDADA...//

// 5.5 Uso de prototype...//
Persona3.prototype.telefono = '5492622469452'; // Agregamos un nuevo atributo al objeto...//
console.log(padre.telefono); // 5.5 El uso de prototype...//
console.log(madre.telefono); // 5.5 El uso de prototype...//
madre.telefono = '5492622578806'; // Se puede modificar o preasignar en el constructor...//
console.log(madre.telefono); // 5.5 El uso de prototype...//

// 5.6 El uso de call... pasa los argumentos//
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+', '+telefono;
        //return this.nombre+' '+this.apellido;// 5.7 Uso de Apply...
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Licenciado', '5492622469452')); 
console.log(persona4.nombreCompleto2.call(persona5, 'Ingeniero', '5492622578806'));

// 5.7 Uso de Apply..pasa un arreglo...//
let arreglo = ['Ingeniero', '5492622868686'];// Creamos el arreglo con dos elementos...//
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));