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

/*Ejercicio 3: const se utiliza para valores constantes que, 
no pueden ser reasignados, es decir, no pueden cambiar su valor...//*/

const fechaNacimiento = 1984;
console.log(fechaNacimiento);
/*fechaNacimiento = 1984;
//console.log(fechaNacimiento);...solo se ejhecuta el console anterior...//
//Si queremos cambiar el valor de una variable va a generar error...//*/

//Evita repetir tu codigo...
//Dry don't repeat yourself...//

let days = 3;
switch (days) {
    case 1:
        console.log('Hoy es lunes');
        break;
    case 2:
        console.log('Hoy es martes');
        break;
    case 3:
        console.log('Hoy es miercoles');
        break;
    case 4:
        console.log('Hoy es jueves');
        break;
    case 5:
        console.log('Hoy es viernes');
        break;
    case 6:
        console.log('Hoy es sabado');
        break;
    case 7:
        console.log('Hoy es domingo');
        break;
    default:
        console.log('Error en el ingreso del dia de la semana');
        break;
}//esta esta en 27 lineas...//

//Esta es la opcion mejorada...//8 lineas...
let days2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));

/*Ejercicio 4: Hacer meses del año, en switch y 
version funcion declarada...//*/

//Estructura Switch...//
let month = 2;
switch (month) {
    case 1:
        console.log('It is January');
        break;
    case 2:
        console.log('It is February');
        break;
    case 3:
        console.log('It is March');
        break;
    case 4:
        console.log('It is April');
        break;
    case 5:
        console.log('It is May');
        break;
    case 6:
        console.log('It is June');
        break;
    case 7:
        console.log('It is July');
        break;
    case 8:
        console.log('It is August');
        break;
    case 9:
        console.log('It is September');
        break;
    case 10:
        console.log('It is October');
        break;
    case 11:
        console.log('It is November');
        break;
    case 12:
        console.log('It is December');
        break;
    default:
        console.log('Error, Invalid month input');
        break;
}

//Dry don't repeat yourself...Evita repetir tu codigo...//

//Funcion Declarada ...//
let months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error('Invalid month input');
    }
    return months[n-1];
}
console.log(getMonth(4));