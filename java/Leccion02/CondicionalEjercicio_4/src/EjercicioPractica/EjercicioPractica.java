package EjercicioPractica;

import java.util.Scanner;

public class EjercicioPractica {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese la primer nota: ");
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
        }
    }
}