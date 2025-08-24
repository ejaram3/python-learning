# ============================================================
#        L – Liskov Substitution Principle (LSP)
# ============================================================
# Principio:
#   "Las subclases deben poder sustituir a sus superclases
#    sin alterar el comportamiento esperado."
#
# Si una clase hija rompe las expectativas de la clase padre,
# entonces viola LSP.
#
# Ejemplo clásico: no todas las aves vuelan. 
# Si forzamos a todas las aves a implementar "volar", 
# tendríamos un problema con las aves no voladoras.

# Clase base genérica
class Ave:
    def comer(self):
        return "Estoy comiendo"


# Subclase para aves que sí vuelan
class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"


# Subclase para aves que no vuelan
class AveNoVoladora(Ave):
    def caminar(self):
        return "Estoy caminando"


# ============================================================
#                  Uso del principio LSP
# ============================================================

def hacer_comer(ave: Ave):
    # Todas las aves deben poder comer sin romper el comportamiento
    print(ave.comer())


# Ejemplos
gorrion = AveVoladora()
pinguino = AveNoVoladora()

# Ambas instancias se comportan correctamente como "Ave"
hacer_comer(gorrion)   # Estoy comiendo
hacer_comer(pinguino)  # Estoy comiendo

# Uso específico sin romper LSP:
print(gorrion.volar())   # Estoy volando
print(pinguino.caminar()) # Estoy caminando