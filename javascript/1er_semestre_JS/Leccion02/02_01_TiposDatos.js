//Tipos de Datos en javascript
/*
La sintaxis en lo que es comentarios
es muy similar en la de Java
realmente diriamos que es identica
*/

//Las variables se pueden cambiar en cualquier momento...//

/*La función typeof, colocada delante de una variable en console.log,
muestra (imprime) el tipo de dato en la consola
y no el valor de la variable.

Por ejemplo, permite saber si una variable es string, number, boolean, etc
*/

//Tipo string...//
var nombre = "Abel"; 
console.log(typeof nombre);
nombre = 7;
console.log(nombre);
nombre = 12.7;
console.log(typeof nombre);

//Tipo number...//
var numero = 3000;
console.log(numero);

//Tipo object...//
var objeto = {//Creamos objeto y agregamos caracteristicas...//
    nombre : "fusil",
    marca : "Mauser",
    calibre : "7.65mm"//No hace falta agregar ultima ","...//
}
console.log(typeof objeto);

//Tipo boolean...//
var bandera = true;
console.log(bandera)

//Tipo function...//
function mifuncion(){}
console.log(mifuncion);

//Tipo symbol...//
var simbolo = Symbol("miSimbolo");
console.log(simbolo);

//Tipo class...//
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//Tipo undefined...//
var x;
//al no asignar una variable por default asigna undefine...//
console.log(typeof x);//funcion typeof asigna undefined marcado...//

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor...//
var y = null;//null no es un tipo de dato, pero su origen es de tipo object...//
console.log(typeof y);

//Tipo de Dato Array y Empty string...//
var autos = ["Ford","Chevrolet","Fiat","Renault"];//array poseen corchetes y comillas....//
console.log(autos);
console.log(typeof autos);//Preguntamos que tipo de dato, es de tipo:

var z ='';
console.log(z);//Esto se refiere a que es una cadena vacia, ¨[Empty string]
//El profesor al ejecutar muestra de tipo [empty string] a mi NO solo ""...//
console.log(typeof z);