
package Ejercicio2;
//Ejercicio 2: Estaciones del año con Sentencia swich...//

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Dighite un numero de mes: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion no encontrada";
        switch(mes){
            case 1: case 2: case 3:
                estacion = "Verano";
                break;
            case 4: case 5: case 6:
                estacion = "Otoño";
                        
                break;
            case 7: case 8: case 9:
                estacion = "Invierno";
                break;
            case 10: case 11: case 12:
                estacion = "Verano";
        }  
        System.out.println("estacion = " + estacion);
    }
}
