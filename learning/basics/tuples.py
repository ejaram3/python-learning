# Tema: Tuplas

"""
Descripción:
Una tupla es una colección ordenada e inmutable que permite elementos duplicados. Es uno de los 4 tipos de estructuras de datos integradas en Python junto con listas, diccionarios y conjuntos. Las tuplas se declaran con paréntesis () y son útiles cuando se desea proteger los datos de modificaciones accidentales.
"""

# Sintaxis básica

tupla_frutas = ("apple", "banana", "cherry")
print(tupla_frutas)

# Permite duplicados
tupla_frutas = ("apple", "banana", "cherry", "apple", "cherry")
print(tupla_frutas)

print(len(tupla_frutas))

# Tupla con un solo elemento
una_fruta = ("apple",)
print(type(una_fruta))

no_tupla = ("apple")
print(type(no_tupla))

# Tipos y constructor

numeros = (1, 2, 3, 4, 5)
booleanos = (True, False, False)
tupla_mixta = ("abc", 34, True, 40, "male")
tupla_constructor = tuple(("apple", "banana", "cherry"))
print(type(tupla_constructor))

# Acceso y slicing

print(tupla_constructor[0])
print(tupla_constructor[-1])

frutas = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(frutas[2:5])
print(frutas[:4])
print(frutas[2:])
print(frutas[-4:-2])

if "apple" in frutas:
    print("Sí, apple está en la tupla")

# Inmutabilidad y soluciones

tupla_origen = ("apple", "banana", "cherry")
lista_temporal = list(tupla_origen)
lista_temporal[1] = "kiwi"
tupla_modificada = tuple(lista_temporal)
print(tupla_modificada)

lista_temporal.append("naranja")
tupla_agregada = tuple(lista_temporal)
print(tupla_agregada)

tupla_concatenada = ("apple", "banana", "cherry") + ("orange",)
print(tupla_concatenada)

lista_eliminar = list(("apple", "banana", "cherry"))
lista_eliminar.remove("cherry")
tupla_final = tuple(lista_eliminar)
print(tupla_final)

# Desempaquetado de tuplas

colores = ("verde", "amarillo", "rojo")
verde, amarillo, rojo = colores
print(verde, amarillo, rojo)

frutas_ext = ("apple", "banana", "cherry", "strawberry", "raspberry")
primero, segundo, *resto = frutas_ext
print(primero, segundo, resto)

frutas_varias = ("apple", "mango", "papaya", "pineapple", "cherry")
primero, *medio, ultimo = frutas_varias
print(primero, medio, ultimo)

# Recorrido de tuplas

for fruta in frutas:
    print(fruta)

for i in range(len(frutas)):
    print(frutas[i])

i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

# Operaciones con tuplas

tupla_letras = ("a", "b", "c")
tupla_numeros = (1, 2, 3)
tupla_combinada = tupla_letras + tupla_numeros
print(tupla_combinada)

frutas_repetidas = ("apple", "banana", "cherry") * 2
print(frutas_repetidas)

# Métodos de tuplas

"""
count() → Cuenta cuántas veces aparece un valor en la tupla
index() → Devuelve el índice de la primera aparición de un valor
"""