# =====================================================
# Tema: Tuplas
# =====================================================

"""
Descripción:
Una tupla es una colección ordenada e inmutable que permite elementos duplicados. Es uno de los 4 tipos de estructuras de datos integradas en Python junto con listas, diccionarios y conjuntos. Las tuplas se declaran con paréntesis () y son útiles cuando se desea proteger los datos de modificaciones accidentales.
"""

# =====================================================
# 1. Sintaxis básica
# =====================================================

# Crear una tupla
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)

# Permite duplicados
this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)

# Longitud
print(len(this_tuple))

# Tupla con un solo elemento
one_item = ("apple",)
print(type(one_item))

not_tuple = ("apple")  # Esto es un str
print(type(not_tuple))

# =====================================================
# 2. Tipos y constructor
# =====================================================

tuple_1 = ("apple", "banana", "cherry")
tuple_2 = (1, 2, 3, 4, 5)
tuple_3 = (True, False, False)
tuple_mixed = ("abc", 34, True, 40, "male")

this_tuple = tuple(("apple", "banana", "cherry"))
print(type(this_tuple))

# =====================================================
# 3. Acceso y slicing
# =====================================================

print(this_tuple[0])           # Primer elemento
print(this_tuple[-1])          # Último elemento

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:5])         # Rango positivo
print(this_tuple[:4])
print(this_tuple[2:])
print(this_tuple[-4:-2])       # Rango negativo

if "apple" in this_tuple:
    print("Sí, apple está en la tupla")

# =====================================================
# 4. Inmutabilidad y soluciones
# =====================================================

# Modificar una tupla → convertir a lista y volver a tupla
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Agregar elementos
x = list(x)
x.append("naranja")
x = tuple(x)
print(x)

# Concatenar tuplas
this_tuple = ("apple", "banana", "cherry")
y = ("orange",)
this_tuple += y
print(this_tuple)

# Eliminar elementos → convertir a lista
this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.remove("cherry")
this_tuple = tuple(y)
print(this_tuple)

# Eliminar completamente
# del this_tuple

# =====================================================
# 5. Desempaquetado de tuplas
# =====================================================

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green, yellow, red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green, tropic, red)

# =====================================================
# 6. Recorrido de tuplas
# =====================================================

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

x = 0
while x < len(fruits):
    print(fruits[x])
    x += 1

# =====================================================
# 7. Operaciones con tuplas
# =====================================================

# Unir
tuple_1 = ("a", "b", "c")
tuple_2 = (1, 2, 3)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

# Repetir
fruits = ("apple", "banana", "cherry")
repeated = fruits * 2
print(repeated)

# =====================================================
# 8. Métodos de tuplas
# =====================================================

"""
count() → Cuenta cuántas veces aparece un valor en la tupla
index() → Devuelve el índice de la primera aparición de un valor
"""

example = ("apple", "banana", "cherry", "apple")
print(example.count("apple"))   # 2
print(example.index("banana"))  # 1
