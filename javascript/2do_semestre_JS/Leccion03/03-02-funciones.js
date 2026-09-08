//03-02-funciones.js ...//
// Javascript - Clase 3 - Leccion03: Funciones...//
//1.1 Introduccion a funciones en Javascript...//
miFunction(8, 2); // Esto se lo conoce como Hosting..//
function miFunction(a, b){
    console.log("Sumamos: "+ (a + b));
}

// Llamamos a la funcion...//
miFunction(5, 4);

// 1.2 Palabra return...// javascrip solo coloca return al final...//
miFunction(8, 2); // Esto se lo conoce como Hosting..//
function miFunction(a, b){
   console.log("Sumamos: "+ (a + b));
   return a + b; // Retorna el valor de la suma...//
}
// Llamamos a la funcion...//
miFunction(5, 4);

let resultado = miFunction(6, 7);
console.log(resultado);

// 1.3 Funcion de tipo expresion anonima...//
// Declaramos una funcion de tpo expresion...//
let x = function(a, b){ return a + b};// Necesita cierre con ; ...//
// La funcion se asigna a una variable...//
resultado = x(5, 6); // Llamamos a la funcion...//
// Al llamarla se pone la variable y parentesis...//
console.log(resultado);   

// 1.4 Funciones de tipo self-invoking...//
(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6); 

// 1.5 Tipos de datos en una función...//
console.log(typeof miFunction); // Devuelve el tipo de dato de la funcion...//  
function miFunctionDos(a, b){
    console.log(arguments.length); 
} // Es una pregunta que nos dice cuantos argumentos tiene la funcion...//

miFunctionDos(5, 7, 3, 6); // Se pueden agregar mas de dos argumentos, pero solo se toman los que estan declarados en la funcion...//

// Metodo toString()...//
var miFunctionTexto = miFunctionDos.toString();
console.log(miFunctionTexto); // Devuelve el codigo de la funcion...//

// 1.6  Funciones flecha...// similar a las de tipo expresion o anonima...//
const sumarFunctionFlecha = (a, b) => a + b; // Se puede omitir la palabra return y las llaves...//
resultado = sumarFunctionFlecha(3, 7); // Asigna el valor de la varible...//
console.log(resultado);
// No se utiliza palabra function, no se utilizan llaves y tampoco return...//

// 1.7 Argumentos y parámetros...//
// (a + b) son los parametros de la funcion...//
// (3, 5) son los argumentos de la funcion...//

// Aqui hemos hecho una funcion de tipo expresion o anonima...//
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); // muestra el parametro a...//
    console.log(arguments[1]); // muestra el parametro b...//
    
    return a + b + arguments[2]; // Retorna el valor de la suma...      
}
resultado = sumar(3, 2, 9); // Asigna el valor de la varible...//
console.log(resultado); // Muestra el resultado de la suma...//
// Si quitamos un argumento da undefined...//

// 1.8 Concepto hoisting...// cuando no usamos funcioon flecha usamos esta...//
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; // arguments es para arreglos...//
    }
    return suma; // Retorna el valor de la suma...
}    

// 1.9 Paso por valor...// Cuando pasamos un valor primitivo a una funcion, se pasa por valor...//
// Tipos primitivos...///
let k = 10;
function cambiarValor(a){ // paso por Valor...//
    a = 20;
}
// la variable k no cambia su valor, porque se paso el valor...//
cambiarValor(k); // Se pasa por valor...//
console.log(k);

// 1.9.1 Paso por referencia...//
const persona = {
    nombre: 'Juan',
    apellido: 'Lopez'
}
console.log(persona);
function cambiarValorObjeto(p1){ // Pasa direccion de memoria hexadecimal...//
    p1.nombre = 'Ignacio';
    p1.apellido = 'Lapúa';
}
// Se destruye la vartiable p1 pero apunta al espacio de memoria persona..//
cambiarValorObjeto(persona); // Se pasa por referencia...//
console.log(persona); // Muestra el objeto con el valor cambiado...//