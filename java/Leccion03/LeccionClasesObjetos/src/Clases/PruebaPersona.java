/*
 
 */
package Clases;

public class PruebaPersona { // PascalCase...//
    public static void main(String[] args) {// Variable: persona1 que es persona(1)...//
        Persona persona1;//Persona persona1 = new Persona(); //se puede poner en - lineas...//
        persona1 = new Persona();// Llamamos al constructor con ()...//
        persona1.nombre = "Abel";// El valor hexadecimal normalmente comienza con 0x...//
        persona1.apellido = "Astudillo";
        persona1.obtenerInformacion();
        // Clase 4.3 Creacion de un Objeto mas...//
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Mia";
        persona2.apellido = "Astudillo";
        persona2.obtenerInformacion();
    }
}
