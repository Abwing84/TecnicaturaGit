
package Ejercicio4;

import java.util.Scanner;//Entiendo que la funcion scanner esta de mas...//
/*//Ejercicio 4: Rectangulo calculo de Area y Perimetro, uso de Operador 
Ternmario pára determinar mayor numero...//*/
public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Medidas del Rectangulo...//
        var base = 10;
        var altura = 8;
        System.out.println("Base: " + base);
        System.out.println("Altura: " + altura);
        
        //Calculo del Area...//
        var area = base * altura;
        System.out.println("Area = " + area);
        
        //Calculo del Perimetro...//
        var perimetro = 2 * (base + altura);
        System.out.println("Perimetro = " + perimetro);
        
        //Utilizo el Operador Ternario...//
        var mayor = (area > perimetro) ? area : perimetro;
        System.out.println("El valor mayor entre Area y Perimetro es: " + mayor);
        
        
    }
}
