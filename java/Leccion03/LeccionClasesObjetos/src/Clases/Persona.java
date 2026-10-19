
package Clases;
// Clase 4.1 Metodos...//
public class Persona { 
    // Atributos de la Clase(Caracteristicas)...//
    public String nombre;// 6.6 POO: PASO POR REFERENCIA, modificamos a public...//
    public String apellido;// 6.6 POO: paso por referencia, modificamos a public...//
    // Metodos de la Clase(Acciones)...//
    public void obtenerInformacion(){ // camelCase
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellidos: "+apellido);
    } 
}
