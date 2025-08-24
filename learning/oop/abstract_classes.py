# ============================================================
#                   Tema: Clases Abstractas
# ============================================================

# En Python, las clases abstractas permiten definir una interfaz
# que otras clases deben implementar. 
# Se usan con el módulo "abc" y el decorador @abstractmethod.
# Una clase abstracta:
#   - No se puede instanciar directamente.
#   - Puede tener métodos abstractos (sin implementación).
#   - Puede tener métodos normales (con implementación).
# Las clases hijas deben implementar los métodos abstractos.

from abc import ABC, abstractmethod


class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    # Método abstracto (obligatorio de implementar en las hijas)
    @abstractmethod
    def hacer_actividad(self):
        pass

    # Método normal (opcional de sobrescribir en las hijas)
    def presentarse(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')


# ------------------------------------------------------------
# Clase hija 1
# ------------------------------------------------------------
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')


# ------------------------------------------------------------
# Clase hija 2
# ------------------------------------------------------------
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy trabajando como {self.actividad}')


# ============================================================
#                  Uso de clases abstractas
# ============================================================

# ❌ Esto genera error porque no se pueden instanciar clases abstractas
# persona = Persona("Elkin", 28, "M", "Algo")

# ✅ Instanciamos clases concretas que implementan los métodos abstractos
elkin = Estudiante('Elkin', 28, 'M', 'Programación')
elkin.hacer_actividad()   # Estoy estudiando: Programación
elkin.presentarse()       # Hola, me llamo Elkin y tengo 28 años

jose = Trabajador('Jose', 22, 'M', 'Obrero')
jose.hacer_actividad()    # Estoy trabajando como Obrero
jose.presentarse()        # Hola, me llamo Jose y tengo 22 años