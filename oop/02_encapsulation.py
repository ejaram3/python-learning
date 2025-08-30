# ============================================================
#                   Tema: Encapsulamiento
# ============================================================

# El encapsulamiento permite "proteger" los atributos y métodos
# de una clase, restringiendo el acceso directo desde fuera.
# En Python no existe un verdadero private, pero se logra usando:
#   - Atributo protegido: _atributo (convención)
#   - Atributo privado: __atributo (name mangling)

class MiClase:
    def __init__(self) -> None:
        # Atributo privado (Python lo renombra internamente)
        self.__atributo_privado = 'valor'

    # Método privado
    def __hablar(self):
        print('Hola, ¿cómo estás?')

    # Métodos públicos para acceder de forma controlada
    def get_atributo(self):
        return self.__atributo_privado
    
    def set_atributo(self, nuevo_valor):
        self.__atributo_privado = nuevo_valor
    
    def hablar_publico(self):
        self.__hablar()


# ============================================================
#                   Uso del Encapsulamiento
# ============================================================

objeto = MiClase()

# ❌ Esto generará error porque __atributo_privado es privado
# print(objeto.__atributo_privado)

# ❌ Esto también dará error porque __hablar es privado
# objeto.__hablar()

# ✅ Acceso controlado mediante métodos públicos
print(objeto.get_atributo())  # valor
objeto.set_atributo("nuevo valor")
print(objeto.get_atributo())  # nuevo valor

# ✅ Acceso indirecto al método privado
objeto.hablar_publico()  # Hola, ¿cómo estás?

# ============================================================
# Nota técnica:
# Python renombra los atributos/métodos privados con name mangling:
#   __atributo  -->  _MiClase__atributo
# Esto hace que aún se puedan acceder forzadamente, pero no es recomendable.
# print(objeto._MiClase__atributo_privado)  # "nuevo valor"