# ============================================================
#                   Tema: Abstracción
# ============================================================

# La abstracción consiste en exponer solo los métodos esenciales
# de un objeto y ocultar los detalles internos de implementación.
# En este ejemplo, el usuario de la clase "Auto" no necesita
# preocuparse por el estado interno: solo llama a "conducir()".

class Auto:
    def __init__(self):
        # Atributo protegido para el estado
        self._estado = 'apagado'

    def encender(self):
        self._estado = 'encendido'
        print('Auto encendido')

    def conducir(self):
        # El detalle de si el auto está apagado o no
        # queda oculto para el usuario de la clase
        if self._estado == 'apagado':
            self.encender()
        print('Conduciendo el auto')


# ============================================================
#                  Uso de la abstracción
# ============================================================

auto = Auto()
auto.conducir()  # El usuario solo pide "conducir" sin preocuparse del estado