
package Ejercicio1;

import java.util.Scanner;//*...//


public class Ejercicio1 {
    public static void main(String[] args) {//psvm+tab clase main...//
        Scanner entrada = new Scanner(System.in);//click izquierdo en el foco y aparece el paquete *...//
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Precio del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println(nombreLibro +" #"+idLibro);
        System.out.println("Precio del libro: $"+ precioLibro);
        System.out.println("El envio del libro gratuito es: "+envioGratuito);
    
    }
 
}
