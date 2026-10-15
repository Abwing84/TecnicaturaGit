
package Operaciones;
/// Clase 5.1 Clase Aritmética: Creamos un objeto.Parte 3 solucion...//
// No es buena practica crear el main dentro de donde creamos 
// la clase y los atributos...//

public class PruebaAritmetica {// Esta en PascalCase...//
    public static void main(String[] args) {
        var a = 10;// variables locales // 6.2 Alcance de variables
        int b = 7;// Memoria stack// 6.3 Engineer Java: Memoria stack 
        miMetodo();// Llamamos el nuevo metodo 6.2 Alcance de variab
        Aritmetica aritmetica1 = new Aritmetica();  
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        //aritmetica1 = null;// esto no se debe utilizar...//
        aritmetica1.sumarNumeros();// Llama al metodo, que estaba sumando (ver clase aritmetica)...//    
     
// Clase 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug...//
// Creamos otro metodo...//
// Para almacenar un objeto o los atributos se utiliza la memoria heap...//
// de arriba 6.3 Engineer Java: Memoria stack y heap...//
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
// Clase 5.3 Paso de argumentos a un método...//        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumnetos = "+resultado);
        // 6.1 Sobrecarga de métodos
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = "+aritmetica2.a);
        System.out.println("aritmetica2 = "+aritmetica2.b);
        // 6.3 Engineer Java: Memoria stack y heap, tratamiento de residuos
        //aritmetica1 = null; el recolector de residuo lo hace automaticamente el compilador
        //System.gc();// Gargbage colector, se utiliza para limpiar residuos del programa
        // es muy pesado y es innecesario...//
    }     
// 6.2 Alcance de variables    
    public static void miMetodo(){// otro metodo // MODULARIDAD...//
        //a = 10;// da error 
        System.out.println("Aqui hay otro metodo");
    }
} 


