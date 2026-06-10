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
        */ 
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
//Se recomineda el nombre que sea descriptivo No muy corto...//

        var a = 8;
        var b = 4; 
        System.out.println(usuario + a + b);
        /*Contexto de cadena, como hay cadena, lo toma a todos como cadena,
        si agrego el parentesis dentro del print hace la concatenacion de la 
        cadena y la operacion de suma...//
        */
        
    }
}
