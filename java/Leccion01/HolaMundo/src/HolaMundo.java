
import java.util.Scanner;

//Nuestro primer programa Hola Mundo...una linea...//
/*
muchas lineas, comentarios extensivos: de muchas lineas
mas 
mas
 */
public class HolaMundo {

    public static void main(String[] args) {
        //Escribe tu codigo desde aqui...//
        /*System.out.println("Hola mundo desde Java");
    
        int miVariable = 10;
        System.out.println(miVariable); 
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en Programación";
        System.out.println(miVariableCadena);
         */
 /*
//Var - inferencia de tipos en Java...//
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //SOUTV + TAB...//
        //Para ejecutar Shift + f6 es la tecla para mayuscula...//

//Reglas para definir una variable en Java...//
        var miVariableEjemplo = 45;
        /* Se recomienda utilizar el tipo de escritura camelCase, 
        No permite numero delante
        No permite caracteres especiales
        No se recomineda poner acento
        Se puede empezar con _ y $ al inicio
        NO se puede usar el # caracter ilegal
        
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        /*Se recomineda el nombre que sea descriptivo No muy corto...//
//Ejercicio: Concatenacion.../
        var a = 8;//reglas def variables
        var b = 4;
        System.out.println(usuario + a + b);
        /*Contexto de cadena, como hay cadena, lo toma a todos como cadena,
        si agrego el parentesis dentro del print hace la concatenacion de la 
        cadena y la operacion de suma con el resultado...//
         
//Ejercicio: Caracteres Especiales con Java...//
        var nombre = "Abel";
        System.out.println("Nueva linea: \n" + nombre);//Salto de linea...//
        System.out.println("Tabulador: \t" + nombre);//Tabulador...//
        System.out.println("\t\t.:MENU:.");//Se pueden unir las Tabulaciones.../
        System.out.println("Retroceso: \b" + nombre);//Caracter Retroceso...//
        System.out.println("Comillas simples: \'" + nombre + "\'");//Comillas simples...//
        System.out.println("Comillas dobles: \"" + nombre + "\"");//Comillas dobles...//
         
//Ejercicio: Clase Scanner...//
        Scanner entrada = new Scanner(System.in);//crea objetos, en este caso llamado entrada...//
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("escriba la profesion: ");
        var profesion2 = entrada.nextLine();
        System.out.println("Resultado = " + profesion2 +" " + usuario2);
        */
//Ejercicio: Detalles del Libro (scanner)...//
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite nombre del Libro: ");
        var libro = entrada.nextLine();
        System.out.println("libro = " + libro);
        System.out.println("Escriba el nombre del autor: ");
        var autor = entrada.nextLine();
        System.out.println("El libro: \"" + libro +"\" fue escrito por " + autor);

    }
}
