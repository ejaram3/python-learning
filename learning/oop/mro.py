# ============================================================
#                   Tema 4: MRO (Method Resolution Order)
# ============================================================
# El MRO define el orden en que Python busca atributos/métodos
# en una jerarquía de herencia. Afecta a:
# 1) Resolución de métodos cuando hay múltiples clases en la jerarquía.
# 2) El comportamiento de super(), que sigue el orden del MRO.

class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    def hablar(self):
        print('Hola desde B')

class F:
    def hablar(self):
        print('Hola desde F')

class H:
    def hablar(self):
        print('Hola desde H')

class E(F, H):
    def hablar(self):
        print('Hola desde E')

class C(E):
    def hablar(self):
        print('Hola desde C')

class D(B, C):
    def hablar(self):
        print('Hola desde D')

# Instancia de D
d = D()

# 1) Llamada normal: usa el método de la clase D (tope de la jerarquía)
d.hablar()  # Hola desde D

# 2) Inspeccionar el MRO de D (orden de búsqueda)
#    Se imprime la cadena de resolución que seguirá Python.
print([cls.__name__ for cls in D.mro()])
# Salida típica: ['D', 'B', 'A', 'C', 'E', 'F', 'H', 'object']

# 3) Llamada directa a un método de una clase específica,
#    pasando la instancia d: se fuerza la implementación de C.
C.hablar(d)  # Hola desde C

# # 4) Demostración de super() siguiendo el MRO:
# #    Redefinimos hablar en D para encadenar llamadas según MRO.
# class D(B, C):
#     def hablar(self):
#         print('Hola desde D')
#         super().hablar()  # Llama al siguiente en MRO después de D

# d2 = D()
# d2.hablar()
# # Salida:
# # Hola desde D
# # Hola desde B
# # (B no usa super(), por eso se detiene allí; si B llamara super(), seguiría A, luego C, E, F, H, object)