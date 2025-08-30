# ============================================================
#                   Tema: Clases y Objetos
# ============================================================

# 1. Definición de una Clase
# Una clase es un molde que define las características (atributos)
# y comportamientos (métodos) que tendrán los objetos creados.
class Carro:

    # 2. Constructor __init__
    # Método especial que se ejecuta al crear una instancia.
    # Se usa para inicializar los atributos del objeto.
    def __init__(self, marca, color, modelo):
        self.marca = marca    # Atributo de instancia
        self.color = color    # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

    # 3. Métodos (comportamientos del objeto)
    def encender(self):
        print(f"Arranco el auto {self.marca}")

    def apagar(self):
        print(f"Se ha apagado el auto {self.marca}")


# ============================================================
#                 4. Creación de Objetos
# ============================================================

# Un objeto es una instancia de la clase.
carro1 = Carro("Audi", "Rojo", "2010")

# ============================================================
#                 5. Uso de los Objetos
# ============================================================

# Acceso a atributos
print(carro1.marca)   # Audi
print(carro1.color)   # Rojo
print(carro1.modelo)  # 2010
carro1.encender()  # Arranco el auto Audi
carro1.apagar()    # Se ha apagado el auto Audi
