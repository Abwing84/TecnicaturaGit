var nombre = 'Jose ';
var apellido = 'Astudillo';
var nombreCompleto = nombre+' '+apellido;//1° concatenacion clasica con +...//
console.log(nombreCompleto);
var nombreCompleto2 = 'Abel'+' '+'Astudillo';//2° concatenacion con valores directos...//
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el nro como string...//
console.log(juntos);
juntos = nombre + 78 + 17;//Aqui se puede diferenciar a traves de parentesis..///
console.log(juntos); 
juntos = 78 + 17 + nombre;
console.log(juntos);
//A esto se lo llama contexto string o contexto cadena...//

nombre += apellido; //3° Concatenacion con el operador simplificado...//
console.log(nombre);

//Hoy ya no se usa var se usa let o const...//
let nombre2 = 'Mia';
console.log(nombre2);

const apellido2 = 'Astudillo';
//apellido2 = "Moran"; Constante no se puede modificar...//
console.log(apellido2);

let x, y; //Se puede crear varias variables en una misma linea...//
x =17, y = 21; //Se puede hacer asignacion de cvarias variables dentro de una misma linea...//
let z = x + y; //Se asigna el valor de la operacion...//
console.log(z);

let _1num = 31;
let $break = 'rompe'; //No utilizar palabras reservadas para variables...//

console.log(_1num);
console.log($break);