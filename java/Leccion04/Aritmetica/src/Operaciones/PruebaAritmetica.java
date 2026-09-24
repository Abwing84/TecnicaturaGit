
package Operaciones;
/// Clase 5.1 Clase Aritmética: Creamos un objeto.Parte 3 solucion...//
// No es buena practica crear el main dentro de donde creamos 
// la clase y los atributos...//

public class PruebaAritmetica {// Esta en PascalCase...//
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica();  
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();// Llama al metodo, que estaba sumando (ver clase aritmetica)...//    
     
// Clase 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug...//
// Creamos otro metodo...//
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
// Clase 5.3 Paso de argumentos a un método...//        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumnetos = "+resultado);
    }         
} 

