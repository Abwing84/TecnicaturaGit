//Ejercicio 1: Calcular estacion del año...//
let mes = 5;//quito comillas para ver si con string que sucede en switch...//
let estacion;
if (mes == 12 || mes == 1 || mes == 2){
    estacion = 'Verano';
}
else if (mes == 3 || mes  == 4 || mes == 5){
    estacion = 'Otoño';
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = 'Invierno';
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = 'Primavera';
}
else {
    estacion ='Valor Incorrecto';
}
console.log('El valor corresponde a la estacion de: ' + estacion);

//Ejercicio 2: Hora del dia...//
let horaDia = 3;
let mensaje;
if(horaDia >= 6 && horaDia < 13){
    mensaje = 'Buenos dias';
}
else if(horaDia >= 13 && horaDia <= 19){
    mensaje = 'Buenas tardes';
}
else if(horaDia >= 20 && horaDia <= 24){
    mensaje = 'Buenas noches';
}
else if(horaDia >= 0 && horaDia <= 5){
    mensaje = 'Dulces Sueños';
}
else{
    mensaje = 'Valor Incorrecto';
}
console.log(mensaje);

/*Estructura Switch(la sintaxis es igual a la de java).
LA COMPARACION ES ESTRICTA, NECESITA QUE LA VARIABLE SIEMPRE SEA NUMERICA...//*/
switch (mes){//No solo se puede utilizar numero, tambien cadenas...//
    case 12 : case 1 : case 2:
        estacion = 'Verano' ;
        break;
    case 3 : case 4 : case 5:
        estacion = 'Otoño' ;
        break;
    case 6 : case 7 : case 8:
        estacion = 'Invierno';
        break;
    case 9 : case 10 : case 11:
        estacion = 'Primavera';
        break;
    default:
    estacion = 'Valor Incorrecto';
}
console.log('El valor corresponde a la estacion de: ' + estacion);
//si asignamos string va generar error, porque la comparacion es estricta...//