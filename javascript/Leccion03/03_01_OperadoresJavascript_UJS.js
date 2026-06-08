//Ejercicio para encontrar numeros pares e impares...//
let parImpar = 10;
if (parImpar % 2 == 0){
    console.log('Es un numero PAR');
}
else{
    console.log('Es un numero IMPAR');
}

//Ejercio es mayor de edad...//
let edad = 18, adulto = 18;
if ( edad >= adulto ){
    console.log('Usted es una persona adulta');
} 
else {
    console.log('Usted es una persona menor de edad');
}

//Ejercico: Dentro de un rango...//
let dentroRango = 10; //Aqui vamos a ir cambiando el valor...//
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('Esta dentro del Rango establecido');
}
else{
    console.log('Esta fuera del Rango establecido');
}

/*
Con var se puede reasignar en cualquier momento, este forma parte del ámbito global.
Un error es que se sobreescriba...
*/
var nombre = "Abel";
nombre = "Juan";
console.log(nombre);

function saludar() {
    var nombre3 = "Natalia";
    console.log(nombre3);
}
// console.log(nombre3) Aqui no lee el dato de la funcion...//

if (true) {
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo.
//Interpreta que la variable está definida, es un fallo...

/*
Let
Puede ser reasignada en cualquier momento, la diferencia es que su ambito es de bloque.
Solo disponible dentro de un bloque de llaves o dentro de una funcion...
*/
function saludar2() {
    let nombre2 = "Abelazo";
    console.log(nombre2);
}
//console.log(nombre2);

if (true) {
    let edad2 = 42;
    console.log(edad2);
}
//console.log(edad2);

/*
Const
Se utiliza para valores constantes que no pueden ser reasignados...
*/
const fechaNacimiento = 1984;
console.log(fechaNacimiento);
//fechaNacimiento = 2009;//No se puede reasignar un valor a una constante, da error...//
//console.log(fechaNacimiento) solo se ejecutaría el log anterior...//s