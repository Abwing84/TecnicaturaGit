// 2° Semestre: Javascript - Clase 1 - Leccion01...//
//1.1 Ciclo while. mientras la condición sea verdadera, se ejecuta el bloque de código ...//
let contador = 0;
while (contador < 3){
    console.log(contador);
    contador++;
}
console.log("fin del ciclo while");

// 1.2 Ciclo do while. primero se ejecuta el bloque de código y luego se evalúa la condición...//
let conteo = 0;
do {
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("fin del ciclo do while");

// 1.3  Ciclo for. se ejecuta un bloque de código un número determinado de veces...//
for(let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("fin del ciclo for");

// 1.4 Palabra reservada break. se utiliza para salir de un ciclo antes de que termine...//
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); // Muestra todos los pares...//
        break; // Rompe el ciclo al encontrar el primer par...//
    }
}
console.log("Termina el ciclo al encontrar los pares");

// 1.5 Palabra reservada continue. se utiliza para saltar a la siguiente iteración del ciclo...//
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; // Salta a la siguiente iteración si el número es impar...// 
    }
    console.log(contando);
}
console.log("Termina el ciclo");

// 1.6 Etiquetas Labels. se utilizan para identificar un ciclo y poder salir de él desde un ciclo anidado...//
inicio: 
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue inicio; // Salta a la siguiente iteración si el número es impar...// 
    }
    console.log(contando);
}
console.log("Termina el ciclo");
// Etiquetas Labels. No son recomendables, programacion go to, se recomienda evitar su uso...// 