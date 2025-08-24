# ============================================================
#   D – Dependency Inversion Principle (DIP)
# ============================================================
# Principio:
#   "Los módulos de alto nivel no deben depender de módulos de bajo nivel,
#    ambos deben depender de abstracciones."
#
# Ejemplo:
#   - Un corrector ortográfico (módulo de alto nivel) NO debería depender
#     directamente de una implementación concreta de verificación.
#   - En su lugar, ambos dependen de una ABSTRACCIÓN (interfaz).
#
# Esto facilita sustituir o extender la lógica sin modificar el corrector.

from abc import ABC, abstractmethod


# ============================================================
#       Abstracción: interfaz que define el contrato
# ============================================================

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra: str) -> bool:
        pass


# ============================================================
#      Implementaciones concretas (módulos de bajo nivel)
# ============================================================

class DiccionarioEspanol(VerificadorOrtografico):
    def verificar_palabra(self, palabra: str) -> bool:
        palabras = {"hola", "adios", "python", "corrector"}
        return palabra.lower() in palabras


class DiccionarioIngles(VerificadorOrtografico):
    def verificar_palabra(self, palabra: str) -> bool:
        words = {"hello", "bye", "python", "checker"}
        return palabra.lower() in words


# ============================================================
#      Módulo de alto nivel (CorrectorOrtografico)
# ============================================================

class CorrectorOrtografico:
    def __init__(self, verificador: VerificadorOrtografico) -> None:
        # Inyectamos la abstracción, no la implementación concreta
        self.verificador = verificador

    def corregir_texto(self, texto: str):
        palabras = texto.split()
        for palabra in palabras:
            if not self.verificador.verificar_palabra(palabra):
                print(f"La palabra '{palabra}' es incorrecta")
            else:
                print(f"La palabra '{palabra}' es correcta")


# ============================================================
#                  Uso del principio DIP
# ============================================================

texto = "hola mundo python bye"

# Corrector con diccionario en español
corrector_es = CorrectorOrtografico(DiccionarioEspanol())
corrector_es.corregir_texto(texto)

print("----")

# Corrector con diccionario en inglés
corrector_en = CorrectorOrtografico(DiccionarioIngles())
corrector_en.corregir_texto(texto)


