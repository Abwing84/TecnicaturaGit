
package CondicionalPractica;

import java.util.Scanner;

public class CondicionalPractica {
    public static void main(String[] args) {
        
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
        System.out.println("Ingrese el primer numero: ");
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
        }   
    }
}
