
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
         
//Ejercicio: Detalles del Libro (scanner)...//
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite nombre del Libro: ");
        var libro = entrada.nextLine();
        System.out.println("libro = " + libro);
        System.out.println("Escriba el nombre del autor: ");
        var autor = entrada.nextLine();
        System.out.println("El libro: \"" + libro + "\" fue escrito por " + autor);
         */
//DATOS PRIMITIVOS ENTEROS...// 
//Ejercicio: Tipo Entero Byte...//
        byte numeroEnteroByte = 127;//Hay perdida de precision...//
        System.out.println("numeroEnteroByte: " + numeroEnteroByte);
        System.out.println("Valor minimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor maximO del Byte:" + Byte.MAX_VALUE);

//Ejercicio: Tipo Entero Short...//
        short numeroEnteroShort = 32767;//precision se pierde, lo muestra negativo...//
        System.out.println("numeroEnteroShort: " + numeroEnteroShort);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);

//Ejercicio: Tipo Entero Int...//
        int numeroEnteroInt = 2147483647;//El entero es muy largo no hay solucion, superar el max de la literal, si agrego 8int)...L se soluciona...//
        System.out.println("numeroEnteroInt: " + numeroEnteroInt);
        System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: " + Integer.MAX_VALUE);

//Ejercicio: Tipo Entero Lon...//
        long numeroEnteroLong = 9223372036854775807L;//Excede la cant. de numeros, por default java toma como int, agregar L...//
        System.out.println("numeroEnteroLong: " + numeroEnteroLong);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: " + Long.MAX_VALUE);

//DATOS PRIMITIVOS FLOTANTES...//
//Ejercicio: Tipo Float...//
        float numFloat = 3.4028235E38F;//Lo toma como double, por eso le agrego el F o (float)adelante...//
        System.out.println("numFloat: " + numFloat);
        System.out.println("Valor minimo de Float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo de Float: " + Float.MAX_VALUE);

//Ejercicio: Tipo Double...//
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble: " + numDouble);
        System.out.println("valor minimo de Double: " + Double.MIN_VALUE);
        System.out.println("Valor maximo de Double: " + Double.MAX_VALUE);

    }
}
