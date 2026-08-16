
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
    }
}
