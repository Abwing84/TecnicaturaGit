
package Ejercicio5;

import java.util.Scanner;
/*//Ejercicio 5: Hacer un programa que calcule e imprima la suma de 
tres calificaciones.
El programa debe solicitar al usuario que ingrese las tres calificaciones.
Crear un nuevo proyecto llamado Ejercicio5....//*/
public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float nota1, nota2, nota3, suma;//Define tipo de variables...//

        // Guardamos las tres notas...//
        System.out.println("Digite las tres calificaciones: ");
        //El usuario ingresa las notas...//
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());

        suma = nota1 + nota2 + nota3;

        System.out.println("\nLa suma es: " + suma);
        
        
    }
}
