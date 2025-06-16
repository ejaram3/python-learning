# =====================================================
# Tema: Listas
# =====================================================

"""
Descripción:
Una lista en Python es una colección ordenada y mutable que permite elementos duplicados. Es uno de los tipos de datos más utilizados para almacenar múltiples elementos en una sola variable. Las listas se pueden indexar, cortar, recorrer, modificar y ordenar.
"""

# =====================================================
# 1. Sintaxis básica
# =====================================================

my_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(my_list))  # Longitud de la lista

list_1 = ["apple", "banana", "cherry"]
list_2 = [1, 2, 3, 4, 5]
list_3 = [True, False, True]
list_mixed = ["abc", 123, True]
print(type(list_mixed))

# Constructor de lista
constructor_list = list(("banana", "apple", "orange"))
print(constructor_list)

# =====================================================
# 2. Acceso y modificación
# =====================================================

list_1 = list(("banana", "apple", "orange"))
print(list_1[0])
print(list_1[-1])

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])
print(this_list[:4])
print(this_list[2:])
print(this_list[-4:-2])

# Verificar existencia
target = "apple"
if target in this_list:
    print(f"{target} existe en la lista")

# Modificar elementos
this_list[0] = "grape"
this_list[1:3] = ["grape", "watermelon"]

# =====================================================
# 3. Inserción y extensión
# =====================================================

this_list = ["banana"]
this_list.insert(1, "grape")
this_list.append("apple")

# extend con listas y otros iterables
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
this_tuple = ("mango", "pineapple")
this_list.extend(this_tuple)

# =====================================================
# 4. Eliminación de elementos
# =====================================================

this_list = ["apple", "banana", "cherry"]
this_list.remove("apple")
this_list.pop(1)
del this_list[0]
this_list.clear()

# =====================================================
# 5. Recorrido de listas
# =====================================================

this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)

for i in range(len(this_list)):
    print(this_list[i])

i = 0
while i < len(this_list):
    print(this_list[i])
    i += 1

# List comprehension
[print(x) for x in this_list]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

numbers = [n for n in range(10) if n < 5]
print(numbers)

upper_fruits = [x.upper() for x in fruits]
print(upper_fruits)

fill_list = ["hello" for _ in fruits]
print(fill_list)

conditional_list = [x if x != "banana" else "apple" for x in fruits]
print(conditional_list)

# =====================================================
# 6. Ordenamiento
# =====================================================

this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)

this_list.sort(reverse=True)
print(this_list)

numeros = [100, 50, 65, 82, 23]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)


def my_func(n):
    return abs(n - 23)


numeros.sort(key=my_func)
print(numeros)

this_list = ["banana", "Orange", "kiwi", "cherry"]
this_list.sort(key=str.lower)
print(this_list)

this_list.reverse()
print(this_list)

# =====================================================
# 7. Copiar listas
# =====================================================

original = ["apple", "banana", "cherry"]
copy_1 = original.copy()
copy_2 = list(original)
copy_3 = original[:]
print(id(original), id(copy_1))

# =====================================================
# 8. Unir listas
# =====================================================

list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
combined = list_1 + list_2
print(combined)

# con bucle
for x in list_2:
    list_1.append(x)
print(list_1)

# con extend
list_1 = ["a", "b", "c"]
list_2 = [1, 2, 3]
list_1.extend(list_2)
print(list_1)

# =====================================================
# 9. Métodos disponibles para listas
# =====================================================

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
