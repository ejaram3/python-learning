# Tema: Listas

"""
Descripción:
Una lista en Python es una colección ordenada y mutable que permite elementos duplicados. Es uno de los tipos de datos más utilizados para almacenar múltiples elementos en una sola variable. Las listas se pueden indexar, cortar, recorrer, modificar y ordenar.
"""

# Sintaxis básica

mi_lista = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(mi_lista))  # Longitud de la lista

lista_1 = ["apple", "banana", "cherry"]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [True, False, True]
lista_mixta = ["abc", 123, True]
print(type(lista_mixta))

# Constructor de lista
lista_constructor = list(("banana", "apple", "orange"))
print(lista_constructor)

# Acceso y modificación

lista_1 = list(("banana", "apple", "orange"))
print(lista_1[0])
print(lista_1[-1])

mi_lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mi_lista[2:5])
print(mi_lista[:4])
print(mi_lista[2:])
print(mi_lista[-4:-2])

objetivo = "apple"
if objetivo in mi_lista:
    print(f"{objetivo} existe en la lista")

mi_lista[0] = "grape"
mi_lista[1:3] = ["grape", "watermelon"]

# Inserción y extensión

mi_lista = ["banana"]
mi_lista.insert(1, "grape")
mi_lista.append("apple")

frutas_tropicales = ["mango", "pineapple", "papaya"]
mi_lista.extend(frutas_tropicales)
tupla_frutas = ("mango", "pineapple")
mi_lista.extend(tupla_frutas)

# Eliminación de elementos

mi_lista = ["apple", "banana", "cherry"]
mi_lista.remove("apple")
mi_lista.pop(1)
del mi_lista[0]
mi_lista.clear()

# Recorrido de listas

mi_lista = ["apple", "banana", "cherry"]
for fruta in mi_lista:
    print(fruta)

for i in range(len(mi_lista)):
    print(mi_lista[i])

i = 0
while i < len(mi_lista):
    print(mi_lista[i])
    i += 1

[print(x) for x in mi_lista]

frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
lista_nueva = [x for x in frutas if "a" in x]
print(lista_nueva)

numeros = [n for n in range(10) if n < 5]
print(numeros)

frutas_mayus = [x.upper() for x in frutas]
print(frutas_mayus)

lista_relleno = ["hello" for _ in frutas]
print(lista_relleno)

lista_condicional = [x if x != "banana" else "apple" for x in frutas]
print(lista_condicional)

# Ordenamiento

mi_lista = ["orange", "mango", "kiwi", "pineapple", "banana"]
mi_lista.sort()
print(mi_lista)

mi_lista.sort(reverse=True)
print(mi_lista)

numeros = [100, 50, 65, 82, 23]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

def mi_func(n):
    return abs(n - 23)

numeros.sort(key=mi_func)
print(numeros)

mi_lista = ["banana", "Orange", "kiwi", "cherry"]
mi_lista.sort(key=str.lower)
print(mi_lista)

mi_lista.reverse()
print(mi_lista)

# Copiar listas

original = ["apple", "banana", "cherry"]
copia_1 = original.copy()
copia_2 = list(original)
copia_3 = original[:]
print(id(original), id(copia_1))

# Unir listas

lista_1 = ["a", "b", "c"]
lista_2 = [1, 2, 3]
combinada = lista_1 + lista_2
print(combinada)

for x in lista_2:
    lista_1.append(x)
print(lista_1)

lista_1 = ["a", "b", "c"]
lista_2 = [1, 2, 3]
lista_1.extend(lista_2)
print(lista_1)

# Métodos disponibles para listas

"""
append()    -> Agrega un elemento al final
clear()     -> Elimina todos los elementos
copy()      -> Devuelve una copia de la lista
count()     -> Cuenta ocurrencias de un valor
extend()    -> Agrega múltiples elementos (lista o iterable)
index()     -> Devuelve el índice del primer valor coincidente
insert()    -> Inserta un elemento en una posición específica
pop()       -> Elimina el elemento en una posición específica
remove()    -> Elimina la primera ocurrencia de un valor
reverse()   -> Invierte el orden de los elementos
sort()      -> Ordena los elementos
"""
