# ============================================================
#              Tema: Decoradores @property
# ============================================================

# El decorador @property en Python permite definir getters,
# setters y deleters de manera más elegante que con métodos explícitos.
# Transforma un método en un "atributo de solo lectura",
# al que luego se le pueden añadir setter y deleter.

class Persona:
    def __init__(self, nombre, edad) -> None:
        # Atributo privado con name mangling
        self.__nombre = nombre
        self._edad = edad

    # -------------------------------
    # Getter con @property
    @property
    def nombre(self):
        return self.__nombre
    
    # -------------------------------
    # Setter con @nombre.setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # -------------------------------
    # Deleter con @nombre.deleter
    @nombre.deleter
    def nombre(self):
        del self.__nombre


# ============================================================
#                  Uso de @property
# ============================================================

persona = Persona('Elkin', 28)

# Acceso como si fuera un atributo (internamente usa el getter)
print(persona.nombre)   # Elkin

# Modificación usando el setter
persona.nombre = 'Jose'
print(persona.nombre)   # Jose

# Eliminación con deleter
del persona.nombre

# ❌ Genera error porque ya se eliminó
# print(persona.nombre)