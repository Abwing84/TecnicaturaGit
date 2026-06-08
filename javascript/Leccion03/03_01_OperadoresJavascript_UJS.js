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

//if (true) {
 //   var edad = 34;
 //   console.log(edad);
//}
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
//console.log(fechaNacimiento) solo se ejecutaría el log anterior...//

// Ejercicio: si el padre puede asistir al juego de su hijo...//
let vacaciones = true, diaLibre = false;
if(vacaciones || diaLibre){
    console.log('El padre puede asistir al juego de su hijo');
}  
else{
    console.log('El padre NO puede asistir al juego de su hijo');
}

//Operador Ternario...//
let resultado2 = 3 > 5 ?  'Verdadero' : 'Falso';
console.log(resultado2);
let numero = 12;
resultado2 = numero % 2 === 0 ? 'Verdadero' : 'Falso';
console.log(resultado2)

//Convertir String a Number...//
let miNumero = '18';//Es una cadena ...//
console.log(typeof miNumero); 
let edad2 = Number(miNumero); //Esta es una funcion ...//
//Funcion is NaN...//
console.log(typeof edad2);
if(isNaN(edad2)){//No es un numeror = is Not a Number (devuelve un resultado Boolean)...//
    console.log('Esta variable no contiene solo numeros');
}
else{
    if(edad2>=18){
    console.log('Puede votar')
    }
    else{
    console.log('Muy joven para votar');
    }
}

//con operador ternario...//
let resultado3 = edad2 >= 18 ? 'Puede votar' : 'Muy joven para votar';
console.log(resultado3);
