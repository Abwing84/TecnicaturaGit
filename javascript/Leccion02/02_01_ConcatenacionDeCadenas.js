var nombre = 'Jose s';
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
