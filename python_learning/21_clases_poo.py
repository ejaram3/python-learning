""" # Tema: Programación Orientada a Objetos (POO)
""" 
#Es una forma similar de relacionar el código a como pensamos en la vida real, permite reutilizar y realizar tareas en menos lineas de código
"""
# Definición de clases
class Perro:
    pass

# Creación del objeto Perro
mi_perro = Perro()  

# Definición de atributos
class Perro:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia 
        self.nombre = nombre
        self.raza = raza

# Creación del objeto 
mi_perro = Perro(nombre="Toby", raza="Bulldog")
print(type(mi_perro))

# Accediendo a los atributos
print(mi_perro.nombre)
print(mi_perro.raza)


# Atributos de clase
class Perro:
    # Atributo de clase
    especie = "mamífero"
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
        self.nombre = nombre
        self.raza = raza

# No necesidad de crear un objeto para acceder al atributo de clase
print(Perro.especie)
# También se puede acceder de esta forma
mi_perro = Perro("Toby", "Bulldog")
print(mi_perro.especie)

# Definición de métodos
class Perro:
    especie = "mamífero"
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    # Métodos
    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

mi_perro = Perro("Toby", "Bulldog")
mi_perro.ladra()
mi_perro.camina(20) """