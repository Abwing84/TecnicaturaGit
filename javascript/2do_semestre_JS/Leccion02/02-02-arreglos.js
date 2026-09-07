// Javascript - Clase 2 - Leccion02: Arreglos...//
//1.1 Arreglos en Javascript,...//
// Creacion de Array o Arreglos...//
//let autos = new Array('Ferrari', 'Renault', 'BMW'); sintaxis antigua de declarar arreglos, No se recomienda...//
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

// 1.2 Recorremos los elementos de un arreglo...//
console.log(autos[0]);
console.log(autos[2]);

for (let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i])
}

// 1.3 Modificar los elementos de un arreglo...//
autos[1] = 'Volvo';
console.log(autos[1]);

// Segunda forma agregamos nuevos valores al arreglo...//
autos.push('Audi'); // Agregamos el elemento al final del arreglo...//
console.log(autos); 

// Otras formas de agregar valores ...//
autos[autos.length] = 'Porsche';
console.log(autos);

// Tercera forma para agregar valores a un arreglo, TENIENDO CUIDADO...//
autos[6] = 'Renault';
console.log(autos) //el arreglo ocupa 4 lugares y al ingresarlo asi desperdiciamos una posicion...//+
// lo que sucede es que deja el espacio vacio y vuelve ineficiente el algoritmo...//

// 1.4 Como preguntar si es un Array o un Arreglo...//
console.log(Array.isArray); // Devuelve un booleano...//

console.log instanceof Array; // = boolean... - Preguntamos si la variable es una instancia de la clase Array...//








