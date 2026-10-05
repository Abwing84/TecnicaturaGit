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
    edad: 30,
    nombreCompleto: function(){ // 1.2 - Metodo o function en javascript
        return this.nombre+' '+this.apellido;
    } // this..... apunta a los atributos o metodos del objeto...//
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
```javascript
// JSON significa JavaScript Object Notation
// Es un formato de texto que se usa para guardar y transmitir datos
// especialmente entre un programa y otro, por ejemplo entre una aplicación y una API.

// Objeto JavaScript
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    edad: 30
};

// En JSON las claves van entre comillas dobles
// Ejemplo:
// {
//     "nombre": "Carlos",
//     "apellido": "Gil",
//     "edad": 30
// }

// En JavaScript también podemos escribir:
// nombre: "Carlos"

// Objeto JavaScript → lo usamos dentro del programa
// JSON → sirve principalmente para intercambiar datos entre programas

// Ejemplo de datos que podría enviar un servidor:
// {
//     "nombre": "Abel",
//     "edad": 42
// }

// JSON no es solamente para JavaScript
// Python, Java, PHP, C#, etc. también pueden leer y generar JSON.

// JSON.stringify()
// Convierte un objeto de JavaScript en texto JSON
let personaJSON = JSON.stringify(persona);

// Muestra el texto JSON
console.log(personaJSON);

// Resultado:
// {"nombre":"Carlos","apellido":"Gil","edad":30}

// OBJETO → JSON (texto)

// JSON.parse()
// Convierte texto JSON en un objeto JavaScript
let personaNueva = JSON.parse(personaJSON);

// Accedemos nuevamente a las propiedades del objeto
console.log(personaNueva.nombre);
console.log(personaNueva.apellido);
console.log(personaNueva.edad);

// Resultado:
// Carlos
// Gil
// 30

// JSON.stringify() → objeto → texto JSON
// JSON.parse() → texto JSON → objeto

// Forma fácil de recordarlo:
// stringify = convertir a string (texto)
// parse = interpretar ese texto y convertirlo nuevamente en objeto

// Importante:
// personaJSON es un texto (string), no un objeto.
// Después de JSON.parse(), personaNueva vuelve a ser un objeto.
```
