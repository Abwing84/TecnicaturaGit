
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
        /*byte numeroEnteroByte = 127;//Hay perdida de precision...//
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
        System.out.println("Valor maximo de Double: " + Double.MAX_VALUE);*/

//Inferencia de tipo var y tipo primitivo...//
        /*var numEntero = 20;//Las literales sin punto automaticamente son de tipo int...//
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F;//Automaticamente con el punto se transforma en tipo double...//
        System.out.println("numFloat = " + numFloat);//pone f detras de la variable...//
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
//Tipos primitivos char...//
        /*ar miVariableChar = 'a';//Solo almacena un caracter y con comillas simples 'a'...//
        System.out.println("miVariableChar = " + miVariableChar);
        char varCaracter = '\u0024';//Indicamos a Java la asignacion con el codigo unicode...//
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36;//Valor decimal del juego de caracteres unicode...//
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';//Un caracter especial, podemos copiar y pegar de unicode...//
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);

        //copy paste y vemnos con var...//
        var varCaracter1 = '\u0024';//Indicamos a Java la asignacion con el codigo unicode...//
        System.out.println("varCaracter = " + varCaracter1);
        var varCaracterDecimal1 = (char)36;//Valor entero y le asigna un tipo int...//
        System.out.println("varCaracterDecimal = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$';//Un caracter especial, podemos copiar y pegar de unicode...//
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';//MUESTRA EL VALOR DECIMAL EN LA VARIABLE TIPO ENTERO ASOCIADO AL SIMBOL UNICODE...
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
//Tipos primitivos - tipos booleanos...//
        /*var varBool = false;//tipo bandera...//
        System.out.println("varBool = " + varBool);
        
        if (varBool){
            System.out.println("La bandera es verde");    
        }//llaves que olvidamos..., la marcamos se enlaza con la que lo abrio...//
        else{
            System.out.println("La bandera es roja");
        }
        //Algoritmo: ¿Es mayor de edad?
        var edad = 18;//Literal tener presente la inferencia de tipo...//
        //var adulto = edad >= 18;//Esta es una expresion booleana...//
        if(edad>= 18){
            System.out.println("Es mayor de edad");
        }
        else{
            System.out.println("Es menor de edad");
        }*/
//Conversion de tipos primitivos en java parte 01...//
        /*var edad = Integer.parseInt("20");//Necesita un string para convertir en entero...//
        System.out.println("edad = " + (edad + 1));

        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);

//Pedir un valor...//
        var entrada = new Scanner(System.in);//scanner activo - metod nextLine funciona...//
        System.out.println("Digite su edad");
//      edad = Integer.parseInt( entrada.nextLine());
//      System.out.println("edad = " + edad);
//Conversion de tipos primitivos en Java pare 02...//Tipo Entero al tipo string...//
        var edadTexto = String.valueOf(10);//tipo de datos entero a string...//
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);//de un string toma un solo caracter...//
        System.out.println("fraseChar = " + fraseChar);
        //el metodo recupera cadena, solo string tiene este metodo...//
      
//Operadores Aritmeticos...//class7
        //SUMA...//
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("Solucion de la suma= " + solucion);
        //RESTA...//
        solucion = num1 - num2;
        System.out.println("Solucion de la resta= " + solucion);
        //MULTIPLICACION...//
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion= " + solucion);
        //DIVISION...//
        solucion = num1 / num2;
        System.out.println("solucion de la division= " + solucion);
        //FLOAT / INT...//
        var solucion2  = 3.4 / num2;
        System.out.println("solucion2 resultado de la division= " + solucion2);
        //RESIDUO DE LA DIVISION...//
        solucion = num1 % num2;//Guarda el residuo entero de la division...//
        System.out.println("solucion = " + solucion);// 
        //NUMERO PAR O IMPAR...//
        if (num2 % 2 == 0)//No es necesario {} porque se utilizan una sola linea de codigo
            System.out.println("Es un numero Par");//la linea de impresion por bloque...//
        else
            System.out.println("Es un numero Impar");*/
    //Operadores de Asignacion...//
        int varNum1 = 3, varNum2 = 4;
        var varNum3 = varNum1 + 6 - varNum2;//una operacion...//
        System.out.println("varNum3 = " + varNum3);
        
    //Operador de Asignacion; tambien se le llama Operador de Composicion...//
        varNum1 += 1; //varNum1 = varNum1 + 1;...//
        System.out.println("varNum1 = " + varNum1);
        
        varNum3 -= 2; //varNum3 = varNum3 - 1;...//
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 *= 4; //varNum2 = varNum2 * 4;...//
        System.out.println("varNum1 = " + varNum1);
        
        varNum1 /= 3; //varNum1 = varNum1 / 3;...//
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 %= 5; //varNum2 = varNum2 % 5;...//
        System.out.println("varNum1 = " + varNum1);
        
        
    }
}    
        
 