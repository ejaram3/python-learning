# ============================================================
#   I – Interface Segregation Principle (ISP)
# ============================================================
# Principio:
#   "Los clientes no deben depender de interfaces que no usan."
#
# Es decir, una clase no debe estar forzada a implementar métodos
# que no le son útiles. 
#
# Ejemplo:
#   - Un humano puede comer, trabajar y dormir.
#   - Un robot solo trabaja (no come ni duerme).
# 
# Si usamos una única interfaz con todos los métodos (comer, trabajar, dormir),
# obligamos a `Robot` a implementar métodos que no usa → viola ISP.
#
# Solución: separar las interfaces en varias más pequeñas.

from abc import ABC, abstractmethod


# ============================================================
#         Interfaces pequeñas y específicas
# ============================================================

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


# ============================================================
#         Clases concretas que implementan lo que necesitan
# ============================================================

class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print('El humano está comiendo')

    def trabajar(self):
        print('El humano está trabajando')

    def dormir(self):
        print('El humano está durmiendo')


class Robot(Trabajador):
    def trabajar(self):
        print('El robot está trabajando')


# ============================================================
#                  Uso del principio ISP
# ============================================================

robot = Robot()
robot.trabajar()      # El robot está trabajando

humano = Humano()
humano.trabajar()     # El humano está trabajando
humano.comer()        # El humano está comiendo
humano.dormir()       # El humano está durmiendo