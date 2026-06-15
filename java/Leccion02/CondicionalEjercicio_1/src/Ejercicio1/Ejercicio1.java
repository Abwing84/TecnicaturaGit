
package Ejercicio1;
//Ejercicio 1: Estaciones del año con if - else...//

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        /*Scanner entrada = new Scanner(System.in);
        
        System.out.println("digite un mes del año");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion desconcoida";
        if (mes == 1||mes == 2||mes == 3){
            estacion = "Verano";
        }    
        else if(mes == 4||mes == 5||mes == 6){
            estacion = "Otoño";
        }    
        else if(mes == 7||mes == 8||mes == 9){
            estacion = "Invierno";
        }
        else if(mes == 10||mes == 11||mes == 12){
            estacion = "Primavera";
        }
        System.out.println("estacion = " + estacion);*/
        
    //Ejercicio: Sentencia de control Switch...//
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero){
            case 1:
                numeroTexto = "Numero uno";
                break;//break controla la sentecia de contro swicth...//
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break; 
            case 4:
                numeroTexto = "Numero cuatro";
                break; 
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }    
}
