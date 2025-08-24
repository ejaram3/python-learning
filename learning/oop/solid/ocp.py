# ============================================================
#              Tema: Principios SOLID en POO
# ============================================================

# ============================================================
#      O – Open/Closed Principle (OCP)
# ============================================================
# Las clases deben estar:
#   - Abiertas a la extensión (se pueden crear nuevas funcionalidades
#     mediante herencia o composición).
#   - Cerradas a la modificación (no se debe cambiar el código
#     de la clase base cada vez que se necesite un nuevo comportamiento).
#
# Ejemplo: un sistema de notificaciones que puede enviar mensajes
# por diferentes canales (Email, SMS, WhatsApp, etc.).
# Si queremos agregar un nuevo canal, no modificamos la clase base,
# simplemente creamos una nueva clase que la extienda.


# Clase base abstracta
class Notificador:
    def __init__(self, usuario, mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError("Debes implementar el método notificar en la subclase")


# Clases hijas que extienden el comportamiento
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando EMAIL a {self.usuario["email"]}: {self.mensaje}')


class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario["sms"]}: {self.mensaje}')


class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f'Enviando WhatsApp a {self.usuario["whatsapp"]}: {self.mensaje}')


# ============================================================
#                  Uso del principio OCP
# ============================================================

usuario = {
    "email": "elkin@example.com",
    "sms": "+573001112233",
    "whatsapp": "+573009998877"
}

mensaje = "Tu pedido ha sido enviado 🚚"

notificadores = [
    NotificadorEmail(usuario, mensaje),
    NotificadorSMS(usuario, mensaje),
    NotificadorWhatsApp(usuario, mensaje)
]

for n in notificadores:
    n.notificar()
