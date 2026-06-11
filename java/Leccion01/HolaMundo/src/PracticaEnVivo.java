
import java.util.Scanner;

public class PracticaEnVivo {

    /*Ejercicio 3: La calificacion final de un estudiante de informática
se calcula con base a las calificaciones de cuatro aspectos de su
rendimiento académico: participación, primer examen parcial, segundo
examen parcial y examen final. Sabiendo que las calificaciones anteriores
entran a la calificación final con ponderaciones de 10%, 25%, 25%
y 40%, Hacer un programa que calcule e imprima la calificación final
obtenida por un estudiante. 
Que el usuario digite las calificaciones de estos 4 datos y así podremos tener,
la calificación final.
     */
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

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

        entrada.close();

    }
}
