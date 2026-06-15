
package Ejercicio6;

import java.util.Scanner;

/*//Ejercicio 6: Guillermo tiene N dólares.
Luis tiene la mitad de lo que posee Guillermo.
Juan tiene la mitad de lo que poseen Luis y Guillermo juntos.
Hacer un programa que calcule e imprima las cantidades de dinero que 
tienen entre los tres.
Crear un nuevo proyecto llamado Ejercicio6...//*/
public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;//Define tipo de variables...//

        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());

        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;//concatenacion...//
        total = luis + guillermo + juan;//concatenacion...//

        System.out.println("\nEl dinero de Luis es: US$" + luis);
        System.out.println("El dinero de Juan es: US$" + juan);
        System.out.println("El total de dinero entre los tres es: US$" + total);
        
        
    }
}
