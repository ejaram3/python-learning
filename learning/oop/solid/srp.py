
# ============================================================
#              Tema: Principios SOLID en POO — SRP
# ============================================================
# S — Single Responsibility Principle (SRP):
# Cada clase debe tener una única responsabilidad o motivo de cambio.
#
# Objetivo:
# - Separar la gestión de combustible del movimiento del auto.
# - Facilitar pruebas, mantenimiento y extensiones (por ejemplo, añadir
#   métricas de consumo sin tocar la lógica de movimiento).

# Esta clase SOLO maneja el combustible
class TanqueCombustible:
    def __init__(self) -> None:
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


# Esta clase SOLO maneja el movimiento del auto
class Auto:
    def __init__(self, tanque: TanqueCombustible):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        # El auto necesita combustible, pero la lógica de manejar
        # el combustible está encapsulada en TanqueCombustible
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print('Has movido el auto exitosamente')
        else:
            print('No hay suficiente combustible')

    def obtener_posicion_auto(self):
        return self.posicion


# ============================================================
#                   Uso del ejemplo SRP
# ============================================================

tanque = TanqueCombustible()
auto = Auto(tanque)

print(auto.mover(10))   # Has movido el auto exitosamente
print(auto.obtener_posicion_auto())  # 10
print(auto.mover(30))   # Has movido el auto exitosamente
print(auto.obtener_posicion_auto())  # 40
print(auto.mover(50))   # Has movido el auto exitosamente
print(auto.obtener_posicion_auto())  # 90
print(auto.mover(100))  # No hay suficiente combustible
print(auto.obtener_posicion_auto())  # 90
print(auto.mover(100))  # No hay suficiente combustible
print(auto.obtener_posicion_auto())  # 90
