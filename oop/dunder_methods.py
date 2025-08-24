# ============================================================
#           Tema: Métodos especiales (Dunder Methods)
# ============================================================

# Los métodos especiales o "dunder" (double underscore) son los que
# Python define con __nombre__. Permiten personalizar el comportamiento
# de los objetos en operaciones comunes como:
#   - Representación en string (__str__, __repr__)
#   - Operadores aritméticos (__add__, __sub__, etc.)
#   - Comparaciones (__eq__, __lt__, etc.)
#   - Iteración (__iter__, __next__), entre otros.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Representación amigable para usuarios (print)
    def __str__(self) -> str:
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

    # Representación oficial para desarrolladores (debugging)
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}", {self.edad})'

    # Sobrecarga del operador +
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)


# ============================================================
#                   Uso de métodos especiales
# ============================================================

elkin = Persona('Elkin', 28)
jose = Persona('Jose', 22)

# __str__ -> se usa cuando hacemos print()
print(elkin)  # Persona(nombre=Elkin, edad=28)

# __repr__ -> se usa para obtener una representación "oficial"
repre = repr(elkin)
print(repre)  # Persona("Elkin", 28)

# Se puede usar eval para reconstruir el objeto a partir del repr
resultado = eval(repre)
print(resultado)  # Persona(nombre=Elkin, edad=28)

# __add__ -> permite usar el operador +
nueva_persona = elkin + jose
print(nueva_persona)       # Persona(nombre=ElkinJose, edad=50)
print(nueva_persona.edad)  # 50
