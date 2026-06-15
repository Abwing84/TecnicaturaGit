
package Ejercicio7;

import java.util.Scanner;
/*//Ejercicio 7: Una compañía de venta de carros usados paga a su personal 
de ventas un salario de 1000 dólares mensuales, más una comisión de 150 
dólares por cada carro vendido, y además el 5% del valor total de las 
ventas realizadas. Cada mes, el capturista de la empresa ingresa en la 
computadora los datos correspondientes.
Hacer un programa que calcule e imprima el salario mensual de un vendedor dado.
El salario base de 1000 dólares debe manejarse como una constante utilizando 
la palabra reservada final.
Crear un nuevo proyecto llamado Ejercicio7....//*/
public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro, porcVenta, totalPrecio;
        //Definio tipo de variables...//
        System.out.print("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());

        System.out.print("Digite el precio de un carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());

        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05F;
        salarioMensual = salario + comision + porcVenta;

        System.out.println("\nEl salario mensual es: " + salarioMensual);
        
    }
}
