
# ============================================================
#                   Tema 2: Herencia Múltiple
# ============================================================

# Clase base 1
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def saludar(self):
        print(f'Hola, soy {self.nombre} de {self.nacionalidad}!')


# Clase base 2
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f'Mi habilidad es: {self.habilidad}'


# Clase derivada (hereda de Persona y Artista)
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # Inicialización explícita de las clases base
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        
        # Nuevos atributos propios de la clase hija
        self.salario = salario
        self.empresa = empresa

    # Sobrescritura (override) de método de la clase Artista
    def mostrar_habilidad(self):
        return 'No tengo jejej'

    # Uso de super() para acceder al método de la clase padre
    def habilidades(self):
        print(f'{super().mostrar_habilidad()}')


# Creación de objeto con herencia múltiple
empleado1 = EmpleadoArtista(
    nombre="Carlos",
    edad=30,
    nacionalidad="Colombiano",
    habilidad="Cantar",
    salario=5000,
    empresa="Sony Music"
)

# Métodos heredados y sobrescritos
empleado1.saludar()                  # De Persona
print(empleado1.mostrar_habilidad()) # Sobrescrito en EmpleadoArtista
empleado1.habilidades()              # Llamada al método original de Artista usando super()