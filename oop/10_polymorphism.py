# ============================================================
#                   Tema: Polimorfismo
# ============================================================

# Polimorfismo = "muchas formas".
# La misma operación (ej: sonido) se comporta de manera distinta
# según el objeto que la implemente.

class Gato:
    def sonido(self):
        return 'Miau'
    
class Perro:
    def sonido(self):
        return 'Guau'
    
gato = Gato()
perro = Perro()

# Función que aplica polimorfismo: acepta cualquier objeto
# que tenga implementado el método sonido()
def hacer_sonido(animal):
    print(animal.sonido())


# Uso del polimorfismo por duck typing
hacer_sonido(gato)   # Miau
hacer_sonido(perro)  # Guau


# ------------------------------------------------------------
# Polimorfismo de Herencia (o polimorfismo de subtipo)
# ------------------------------------------------------------
class Animal:
    def sonido(self):
        return "Sonido genérico"

class GatoHerencia(Animal):
    def sonido(self):
        return "Miau desde herencia"

class PerroHerencia(Animal):
    def sonido(self):
        return "Guau desde herencia"

# Todos son del tipo Animal, pero cada uno responde diferente
animales = [GatoHerencia(), PerroHerencia()]

for animal in animales:
    print(animal.sonido())
    # Cada objeto ejecuta su propia versión del método sonido()