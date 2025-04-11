# Actividad 2: Patrones Estructurales Proxy y Decorator
## Parte 1: Investigación

### ¿Cuál es la principal diferencia entre el patrón Decorator y el patrón Proxy?
La principal diferencia es que el Decorator aumenta o modifica el comportamiento de un objeto de forma dinámica (agregando responsabilidades), manteniendo su interfaz; mientras que el Proxy controla el acceso aun objeto (sin modificar su comportamiento), actuando como un intermediario.

### ¿En qué tipo de escenarios usarías cada uno?
Algunos ejemplos para lo que los usaría son:

Decorator:
- añadir funciones a objetos específicos sin modificar su código original
- combinar muchas capacidades diferentes sin crear muchas subclases

Proxy: 
- controlar quién puede acceder a un objeto
- retrasar la creación de objetos hasta que realmente se necesiten
- guardar resultados para no repetir cálculos 
- registrar el uso de un objeto

## Parte 2: Implementación
Implementé la opción de decorator, obteniendo el siguiente resultado: 
```
Pedido: Espresso + Leche + Canela
Precio: $2.75
```
