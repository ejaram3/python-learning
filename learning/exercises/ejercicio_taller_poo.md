# 🚗 Ejercicio: Sistema de Gestión de Vehículos de un Taller Mecánico

## Requerimientos

### 1. Clases y objetos

-   Crea una clase base `Vehiculo` con atributos como `marca`, `modelo`,
    `anio`.
-   Implementa métodos básicos como `arrancar()` y `detener()`.

### 2. Herencia y polimorfismo

-   Crea subclases `Auto`, `Moto` y `Camion`, que hereden de `Vehiculo`.
-   Sobrescribe el método `arrancar()` con comportamientos diferentes.

### 3. Encapsulación y getters/setters

-   Agrega un atributo privado `_kilometraje` con un getter y setter que
    valide que no se asignen valores negativos.

### 4. Abstracción y clases abstractas

-   Define una clase abstracta `Servicio` con un método abstracto
    `realizar()`.
-   Implementa clases concretas como `CambioAceite` y `RevisionFrenos`.

### 5. Decoradores y property

-   Usa `@property` para calcular el **valor de reventa** de un vehículo
    en función de su año.
-   Implementa un decorador que loguee cada vez que se realiza un
    servicio a un vehículo.

### 6. Dunder methods

-   Implementa `__str__` para que un vehículo se muestre en formato
    legible.
-   Implementa `__eq__` para comparar vehículos por marca y modelo.

### 7. Principios SOLID

-   **SRP**: La clase `Vehiculo` solo se encarga de la representación
    del vehículo, no de servicios.
-   **OCP**: Los nuevos servicios deben poder añadirse sin modificar
    código existente.
-   **LSP**: Los objetos de `Auto`, `Moto` y `Camion` deben poder usarse
    donde se espera un `Vehiculo`.
-   **ISP**: Si agregas interfaces (abstractas) deben ser específicas
    (ej: `ServicioMantenimiento` en lugar de una interfaz gigante).
-   **DIP**: La clase `Taller` debe depender de abstracciones
    (`Servicio`) y no de implementaciones concretas.

### 8. Ejercicio final

-   Crea un `Taller` que reciba una lista de vehículos y servicios.
-   Aplica servicios a los vehículos usando las abstracciones.
-   Muestra en pantalla el resultado de los servicios y el valor de
    reventa de los vehículos.
