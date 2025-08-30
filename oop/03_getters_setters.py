# ============================================================
#                   Tema: Getters y Setters
# ============================================================

# Los getters y setters son métodos usados para:
#   - Obtener el valor de un atributo privado o protegido (getter).
#   - Modificar el valor de un atributo privado o protegido (setter).
# Esto permite controlar cómo se accede y modifica el estado interno
# de un objeto.

class Persona:
    def __init__(self, nombre, edad) -> None:
        # Usamos "_" para indicar que son atributos protegidos
        self._nombre = nombre
        self._edad = edad

    # -------------------------------
    # Getter
    def get_nombre(self):
        return self._nombre

    # Setter
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


# ============================================================
#                   Uso de Getters y Setters
# ============================================================

persona = Persona('Elkin', 21)

# Usando el getter
print(persona.get_nombre())  # Elkin

# Usando el setter para modificar el nombre
persona.set_nombre('Jose')

# Confirmar cambio con el getter
print(persona.get_nombre())  # Jose