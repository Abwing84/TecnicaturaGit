
package CondicionalPractica;

import java.util.Scanner;

public class CondicionalPractica {
    public static void main(String[] args) {
        ///CLASE 9 ...//
        //Ejercicio 1: Estructura if - else...//
        Scanner entrada = new Scanner(System.in);
        /*System.out.println("Ingrese la primer nota: ");
        var notaPrimera = Integer.parseInt(entrada.nextLine());

        System.out.println("Ingrese la segunda nota: ");
        var notaSegunda = Integer.parseInt(entrada.nextLine());

        System.out.println("Ingrese la tercera nota: ");
        var notaTercera = Integer.parseInt(entrada.nextLine());

        var promedio = (notaPrimera + notaSegunda + notaTercera) / 3.0;

        System.out.println("Promedio = " + promedio);

        if (promedio >= 70) {
            System.out.println("El alumno Aprueba");
        } else {
            System.out.println("El alumno Desaprueba");
        }*/
        
        //Ejercicio 2: Descuento de 20%...//
        /*System.out.println("Ingrese el valor de la compra realizada: ");
        var compra = Double.parseDouble(entrada.nextLine());
        
        if(compra >= 100){
            double descuento = compra * 0.20;
            System.out.println("Valor de la compra es: " + (compra - descuento));
        }
        else{
            double descuento = 0;
            System.out.println("Valor de la compra es: " + compra);
        }*/
        
        /*//Ejercicio 3: Lee dos numeros, si son iguales multiplica, si el 1° > 2° 
        resta y sino suma...//*/
        /*System.out.println("Ingrese el primer numero: ");
        var numUno = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el segundo numero. ");
        var numDos = Integer.parseInt(entrada.nextLine());
        
        if(numUno == numDos){
            int resultado = numUno * numDos;
              System.out.println("El Resultado es: " + resultado);      
        }
        else if(numUno > numDos){
            int resultado = numUno - numDos;
            System.out.println("El Resultado es: " + resultado);
        }
        else{
            int resultado = numUno + numDos;
            System.out.println("El Resultado es: " + resultado);
        }*/ 
        
        //CLASE 10...//
//        Ejercicio 1: Construir un programa que, dado un número total de
//        horas, devuelve el número de semanas, días y horas equivalentes.
//        Por ejemplo dado un total de 1000 horas debe mostrar 5 semanas,
//        6 días y 16 horas....//
        
        /*System.out.print("Ingrese el valor de a: ");
        double a = entrada.nextDouble();

        System.out.print("Ingrese el valor de b: ");
        double b = entrada.nextDouble();

        double aCuadrado = Math.pow(a, 2);
        double bCuadrado = Math.pow(b, 2);
        double multiplicacionAb = 2 * a * b;

        double resultado = aCuadrado + bCuadrado + multiplicacionAb;

        System.out.println("(" + a + " + " + b + ")^2 = " + resultado);
        System.out.println("Aplicando la fórmula: " + aCuadrado + " + "
                + bCuadrado + " + " + multiplicacionAb + " = " + resultado);

        double comprobacion = Math.pow(a + b, 2);
        System.out.println("Comprobación directa (a+b)^2 = " + comprobacion);*/

//        Ejercicio 2: Hacer un programa que calcule el cuadro de una suma,
//        el usuario debe ingresar el valor de a y el valor de b.
//        Formula: (a+b)2=a2+b2+2*a*b
//        Para esto deberán utilizar la clase Math y un método llamado pow...//

        /*System.out.println("Ingrese el numero total de horas: ");
        int totalHoras = entrada.nextInt();

        final int horasDia = 24;
        final int diasSemana = 7;
        final int horasSemana = horasDia * diasSemana;

        int semanas = totalHoras / horasSemana;
        int restoHoras = totalHoras % horasSemana;
        int dias = restoHoras / horasDia;
        int horas = restoHoras % horasDia;

        System.out.println(totalHoras + " horas equivalen a:");
        System.out.println("Semanas: " + semanas);
        System.out.println("Dias: " + dias);
        System.out.println("Horas: " + horas);*/

//        Ejercicio 3: La calificacion final de un estudiante de informática
//        se calcula con base a las calificaciones de cuatro aspectos de su
//        rendimiento académico: participación, primer examen parcial, segundo
//        examen parcial y examen final. Sabiendo que las calificaciones anteriores
//        entran a la calificación final con ponderaciones de 10%, 25%, 25%
//        y 40%, Hacer un programa que calcule e imprima la calificación final
//        obtenida por un estudiante. 
//        Que el usuario digite las calificaciones de estos 4 datos y así podremos tener,
//        la calificación final.

        //Ingreso la nota...//
        System.out.print("Ingrese la nota de participación: ");
        double participacion = entrada.nextDouble();

        System.out.print("Ingrese la nota del primer parcial: ");
        double parcial_1 = entrada.nextDouble();

        System.out.print("Ingrese la nota del segundo parcial: ");
        double parcial_2 = entrada.nextDouble();

        System.out.print("Ingrese la nota del examen final: ");
        double examenFinal = entrada.nextDouble();

        //Se sacan los porcentajes correspondientes...//
        double notaFinal = (participacion * 0.10)
                + (parcial_1 * 0.25)
                + (parcial_2 * 0.25)
                + (examenFinal * 0.40);

        System.out.println("La calificación final es: " + notaFinal);
    }
}
