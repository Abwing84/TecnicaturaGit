
package Operaciones;
// Clase 4.6 Creaciones de Metodos...//
// Creamos la carpeta leccion 4 un poco mas directamente...//
public class Aritmetica {
    // Atributos de la clase...//
    int a;
    int b;
    
    // Constructor es un metodo especial...// 6.1 Sobrecarga de métodos
    public Aritmetica(){// Constructor 1 VACIO...//
        System.out.println("Se esta ejecutando el constructor N°1");  
    }
    // Estamos viendo lo que se llama sobrecarga de constructores...//
    public Aritmetica(int a, int b){// Constructor 2...//
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor N°2");
    }
            
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

// Clase 6 Programación Orientada a Objetos Parte 4 Solución
// 6.1 Sobrecarga de métodos
 // Constructor es un metodo especial...//
    //1.construye un objeto
    //2.reserva un espacio de memoria
    //3.inicializa los atributos de la clase

// 6.3 Engineer Java: Memoria stack y heap, tratamiento de residuos...//
