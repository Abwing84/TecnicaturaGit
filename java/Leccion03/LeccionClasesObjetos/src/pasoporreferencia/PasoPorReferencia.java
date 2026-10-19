/*
 // 6.6 POO: PASO POR REFERENCIA...//
clase 06:  en Leccion 3 en LeccionClasesObjetos
new package
 */
package pasoporreferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();// Importamos clase Persona....//
        persona1.nombre = "Esther";// cambiamos a public en case Persona...//
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: "+ persona1.nombre);
        // Cambio al poner el ".nombre": no muestra el espacio de memoria heap y muestra 
        //lo que modificamos(nombre
        // 6.7 Palabras return y null
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = new Persona();
        Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
        //System.out.println("El nuevo valor del objeto es: "+persona2.nombre);
//CAMBIAMOS EL COMENTADO PARA VER LA DOS OPOCIONES DE IMPRESION...//  
    }
        
    public static void cambiarValor(Persona persona){// Paso por Referencia...//
        persona.nombre = "Maria";
        //return ; lo crea solo ...//
    }
    // 6.7 Palabras return y null
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es invalido: Null");
            return null;
        }
        else{
            persona.nombre = "Monica";
            return persona;
        }   
    }
}
