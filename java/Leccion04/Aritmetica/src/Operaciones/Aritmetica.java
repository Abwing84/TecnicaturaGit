
package Operaciones;
// Clase 4.6 Creaciones de Metodos...//
// Creamos la carpeta leccion 4 un poco mas directamente...//
public class Aritmetica {
    // Atributos de la clase...//
    int a;
    int b;
    
    // Metodo...//
    public void sumarNumeros(){// Este metodo no retorna nada...//
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
// Clase 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug...//
// Creamos otro metodo...//
    public int sumarConRetorno(){// Este metodo retorna el valor...//
        //int resultado = a + b;
        return this.a + this.b;
    }
    
// Clase 5.3 Paso de argumentos a un método...//    
    public int sumarConArgumentos(int a, int b){
        this.a = a;// El argumento a se asign al atributo this.a...//
        this.b = b;
        //return a + b;
// Clase 5.4 Un método llamando a otro método...//        
        return this.sumarConRetorno();// Siempre dentro de la misma clase...//
// Clase 5.5 Operador this...EL USO ES OPCIONAL//        
// Solo hace que el codigo sea mas legible, y diferencia el atributo del argumento...//
// Agregue el this. en el metodo de arriba...//
    }
}
 