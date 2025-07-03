# Tema: Conjuntos

"""
Los conjuntos son inmutables, pero se pueden eliminar y agregar elementos.
No están ordenados.
"""

# Constructor
conjunto = set(("apple", "banana", "cherry"))
print(conjunto)

mi_conjunto = {"apple", "banana", "cherry"}
print(type(mi_conjunto))

# No permite duplicados
mi_conjunto = {"apple", "banana", "cherry", "apple"}
print(mi_conjunto)

# True y 1 se consideran iguales en conjuntos
conjunto = {"apple", "banana", "cherry", True, 1, 2}
print(conjunto)

# False y 0 se consideran iguales en conjuntos
conjunto = {"apple", "banana", "cherry", False, 0, 2}
print(conjunto)

# Longitud del conjunto
print(len(conjunto))

# Elementos de diferentes tipos
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {1, 5, 7, 9, 3}
conjunto_3 = {True, False, False}

conjunto_mixto = {"abc", 34, True, 40, "male"}
print(conjunto_mixto)

# Acceso a elementos
conjunto = {"apple", "banana", "cherry"}
for elemento in conjunto:
    print(elemento)

print("banana" in conjunto)
print("banana" not in conjunto)

# Agregar elementos
conjunto = {"apple", "banana", "cherry"}
conjunto.add("orange")
print(conjunto)

# Agregar otro conjunto
conjunto = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
conjunto.update(tropical)
print(conjunto)

# Agregar un iterable
conjunto = {"apple", "banana", "cherry"}
lista = ["kiwi", "orange"]
conjunto.update(lista)
print(conjunto)

# Eliminar elementos
conjunto.remove("kiwi")
print(conjunto)

conjunto.discard("kiwi")  # No lanza error si no existe
print(conjunto)

# Vaciar el conjunto
conjunto = {"apple", "banana", "cherry"}
conjunto.clear()
print(conjunto)

# Eliminar conjunto completamente
conjunto = {"apple", "banana", "cherry"}
# del conjunto
# print(conjunto)

# Recorrer elementos
conjunto = {"apple", "banana", "cherry"}
for elemento in conjunto:
    print(elemento)

conjunto_a = {"a", "b", "c"}
conjunto_b = {1, 2, 3}

# Unión de conjuntos
union_1 = conjunto_a.union(conjunto_b)
unión_2 = conjunto_a | conjunto_b
print(union_1)
print(unión_2)

# Unión múltiple
conjunto_1 = {"a", "b", "c"}
conjunto_2 = {1, 2, 3}
conjunto_3 = {"John", "Elena"}
conjunto_4 = {"apple", "bananas", "cherry"}
conjunto_union = conjunto_1.union(conjunto_2, conjunto_3, conjunto_4)
print(conjunto_union)

conjunto_total = conjunto_1 | conjunto_2 | conjunto_3 | conjunto_4

# Unión con tupla
conjunto_1 = {"a", "b", "c"}
tupla = (1, 35, 5)
union_tupla = conjunto_1.union(tupla)
print(union_tupla)

# update() modifica el conjunto existente
conjunto_1 = {"a", "b", "c"}
conjunto_2 = {1, 2, 3, 4}
conjunto_1.update(conjunto_2)
print(conjunto_1)

# Intersección
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}
interseccion = conjunto_1.intersection(conjunto_2)
print(interseccion)

interseccion_2 = conjunto_1 & conjunto_2
print(interseccion_2)

conjunto_1.intersection_update(conjunto_2)
print(conjunto_1)

# Diferencia
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}
diferencia = conjunto_1.difference(conjunto_2)
print(diferencia)

diferencia_2 = conjunto_1 - conjunto_2
print(diferencia_2)

conjunto_1.difference_update(conjunto_2)
print(conjunto_1)

# Diferencia simétrica
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}
dif_sim = conjunto_1.symmetric_difference(conjunto_2)
print(dif_sim)

dif_sim_2 = conjunto_1 ^ conjunto_2
print(dif_sim_2)

conjunto_1.symmetric_difference_update(conjunto_2)
print(conjunto_1)

"""
add() Añade elementos al set
clear() Remueve todos los elementos del set
difference() retorna los elementos del primer set menos los del segundo set
difference_update() remueve los elementos comunes del segundo set
discard() elimina un elemento si existe
intersection() devuelve los elementos comunes
intersection_update() conserva solo los elementos comunes
isdisjoint() devuelve True si los sets no tienen elementos en común
issubset() devuelve True si el primer set está contenido en el segundo
issuperset() devuelve True si el primer set contiene al segundo
pop() elimina un elemento aleatorio
remove() elimina un elemento si existe, lanza error si no
symmetric_difference() elementos que están en un solo set
symmetric_difference_update() igual que el anterior pero modifica el original
union() une dos o más sets
update() añade elementos de otros iterables
"""
