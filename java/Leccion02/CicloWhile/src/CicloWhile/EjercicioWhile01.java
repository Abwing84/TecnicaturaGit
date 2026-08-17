
package CicloWhile;

public class EjercicioWhile01 {
// Ciclo while: verifica la condicion y si es verdadera ejecuta el codigo...//
    public static void main(String[] args) {
        var conteo = 0;// Inferencia de tipos...//
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;// Vamos aumentoando en uno la variable...//
        }
// Ciclo do while: se ejecuta una vez el codigo y verifica luego la condicion si es verdadera, si la condicion 
        // sigue siendo verdadera se sigue ejecutando el codigo...//
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);// poner punto y coma...//
        
// Ciclo for: numero determinado de iteraciones, tambien tiene una condicion si es verdadera se ejecuta dentro 
        // el codigo.../// 
        for(var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);  
        }
// Palabra break: rompe un ciclo, ponemos los numeros pares, cuando se cumpla la condicion se rompe...//
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
        }    
// Palabra continue: cuando encuentra un numero impar continua no entra a la estructura e imprime el numero par...//
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
                continue; // Vamos a la siguiente iteración...//   
            }
                System.out.println("contando = " + contando);            
        }    
// Uso de Etiquetas: Labels... NO ES BUENA PRACTICA - PROGRAMACION GO TO//
// Se utiliza en ciclos anidados, se colocan adelante del codigo, y luego de la palabra...//
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;
            }
        } 
    }
}
