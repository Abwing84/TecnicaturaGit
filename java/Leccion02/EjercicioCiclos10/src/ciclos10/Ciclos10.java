// 6.8 Ejercicio Ciclos 10: Con Scanner y JOptionPane
// Ejercicio 10: Pedir 10 numeros y escribir la suma total
// Con Scanner ahora...//
package ciclos10;

import java.util.Scanner;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner secuencia = new Scanner(System.in);
        int numero, suma = 0;
        for(int i = 1; i <= 10; i++){
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(secuencia.nextLine());
            suma += numero;
        }
        System.out.println("\nLa suma de toda la Secuencia es: "+suma);
    }
}
