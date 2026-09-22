/*
Ejercicio 6: Pedir numeros hasta que se teclee un 0, 
mostrar la suma de todos los numeros introducidos...// 
tarea hizo p
*/
package Ciclos06;
// Clase 4.5 Ejercicio 6 con Ciclos Clase Scanner y JOptionPane...//*
import javax.swing.JOptionPane;

public class Ejercicio06 {
    public static void main(String[] args) {
        
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero= "));
            suma+= numero;
        }while(numero != 0);
        JOptionPane.showInputDialog(null, "La suma de todos los numeros ingresados es: "+suma);
    }      
}
