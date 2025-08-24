# ============================================================
#                   Tema: Decoradores
# ============================================================

# Un decorador es una función que recibe otra función como parámetro,
# la modifica o extiende, y retorna una nueva función.
# Se usan para añadir comportamiento extra SIN alterar el código original.

def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar a la función')
        funcion()  # Llamada a la función original
        print('Después de ejecutar la función')
    return funcion_modificada


# ------------------------------------------------------------
# Uso sin el azúcar sintáctico (@decorador)
# ------------------------------------------------------------
# def saludo():
#     print('Hola mundo')
#
# saludo_modificado = decorador(saludo)
# saludo_modificado()


# ------------------------------------------------------------
# Uso con el decorador directamente (@decorador)
# ------------------------------------------------------------
@decorador
def saludo():
    print('Hola mundo desde Python')


# Cuando se llama, en realidad se ejecuta la función modificada
saludo()

# Salida:
# Antes de llamar a la función
# Hola mundo desde Python
# Después de ejecutar la función