# =====================================================
# SECCIÓN 1: Sintaxis y creación de listas
# =====================================================

# 1. Crea una lista con 5 nombres de frutas y muéstrala en pantalla.
fruits = ["mango", "pera", "manzana", "uva", "melon"]

# 2. Crea una lista mixta con un número, una cadena, y un valor booleano.
list_mix = ["hola", True, 2]

# 3. Usa el constructor list() para crear una lista con los números del 1 al 3.
numbers = list((1, 2, 3))

# 4. Crea una lista con elementos duplicados y muestra cuántos elementos tiene usando len().
list_with_dups = ["mango", "uva", "melon",
                  "pera", "manzana", "uva", "melon", "pera"]
print(len(list_with_dups))
# =====================================================
# SECCIÓN 2: Acceso y modificación
# =====================================================

# 5. Muestra el primer y último elemento de una lista de frutas.
fruits = ["mango", "pera", "manzana", "uva", "melon"]
print(fruits[0])
print(fruits[-1])

# 6. Accede a los elementos del índice 2 al 4 en una lista de 6 elementos.
fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "grape"]
print(fruit_list[2:4])

# 7. Verifica si la palabra "kiwi" existe en una lista.
print("kiwi" in fruit_list)

# 8. Cambia el segundo elemento de la lista por "sandía".
fruit_list[1] = "sandía"
print(fruit_list)

# 9. Cambia los tres primeros elementos de una lista por ["uva", "melón", "pera"].
fruit_list = ["apple", "banana", "cherry", "orange", "kiwi", "grape"]
update_list = ["uva", "melón", "pera"]
fruit_list[0:2] = update_list
print(fruit_list)

# =====================================================
# SECCIÓN 3: Agregar elementos
# =====================================================

# 10. Inserta "limón" en la posición 2 de una lista.
fruit_list = ["uva", "melón", "pera", "cherry", "orange", "kiwi", "grape"]
fruit_list.insert(2, "limón")
print(fruit_list)

# 11. Agrega "mandarina" al final de una lista con append().
fruit_list.append("mandarina")
print(fruit_list)

# 12. Usa extend() para añadir una lista de verduras al final de una lista de frutas.
fruit_list = ["uva", "melón", "limón", "pera",
              "cherry", "orange", "kiwi", "grape", "mandarina"]
vegetable_list = ["carrot", "broccoli",
                  "spinach", "lettuce", "cucumber", "pepper"]
fruit_list.extend(vegetable_list)
print(fruit_list)

# 13. Extiende una lista con una tupla que contenga al menos dos elementos.
item_list = ["book", "chair", "phone", "key", "backpack", "pen"]
mixed_tuple = ("carrot", 42, True, 3.14, None, "data")
item_list.extend(mixed_tuple)
print(item_list)

# =====================================================
# SECCIÓN 4: Eliminar elementos
# =====================================================

# 14. Elimina el elemento "manzana" de una lista con remove().
fruit_list = ["uva", "melón", "pera", "cherry",
              "orange", "kiwi", "grape", "manzana"]
fruit_list.remove("manzana")
print(fruit_list)

# 15. Usa pop() para eliminar el segundo elemento de la lista.
fruit_list.pop(1)
print(fruit_list)

# 16. Elimina el primer elemento usando del.
del fruit_list[0]
print(fruit_list)

# 17. Limpia toda la lista usando clear().
fruit_list.clear()
print(fruit_list)

# =====================================================
# SECCIÓN 5: Recorrido y comprensión de listas
# =====================================================

# 18. Recorre una lista de frutas con un for y muestra cada una.
fruit_list = ["uva", "melón", "pera", "cherry",
              "orange", "kiwi", "grape", "manzana"]
for x in fruit_list:
    print(x)

# 19. Recorre una lista usando un bucle while y muestra cada elemento.
x = 0
while x < len(fruit_list):
    print(fruit_list[x])
    x += 1

# 20. Usa list comprehension para crear una lista con las frutas que contienen la letra "a".
contains_letter_a = [x for x in fruit_list if "a" in x]
print(contains_letter_a)

# 21. Crea una lista con los cuadrados de los números del 0 al 9 usando list comprehension.
[print(n, "=", n**2)for n in range(10)]

# 22. Crea una nueva lista en la que reemplaces "banana" por "manzana" en otra lista.
fruit_list = ["uva", "melón", "pera", "cherry",
              "orange", "kiwi", "grape", "manzana", "banana"]
fruit_list = ["manzana" if fruit ==
              "banana" else fruit for fruit in fruit_list]
print(fruit_list)

# =====================================================
# SECCIÓN 6: Ordenamiento y reversa
# =====================================================

# 23. Ordena alfabéticamente una lista de frutas.
fruit_list = ["uva", "melón", "pera", "cherry",
              "orange", "kiwi", "grape", "manzana", "banana"]
fruit_list.sort()
print(fruit_list)

# 24. Ordena una lista de números de mayor a menor.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

# 25. Usa una función personalizada para ordenar una lista de números por su cercanía al número 10.


def sort_by_proximity(n):
    return abs(n - 10)


numbers = [27, 84, 10, 63, 92, 6, 38, 74, 59, 41]
numbers.sort(key=sort_by_proximity)
print(numbers)

# 26. Usa sort(key=str.lower) para ordenar ["banana", "Kiwi", "Manzana", "naranja"] sin errores por mayúsculas.
fruits = ["banana", "Kiwi", "Manzana", "naranja"]
fruits.sort(key=str.lower)
print(fruits)

# 27. Invierte una lista con reverse().
fruits.reverse()
print(fruits)

# =====================================================
# SECCIÓN 7: Copiar listas
# =====================================================

# 28. Copia una lista usando copy() y muestra que las IDs son distintas.
fruits = ["banana", "Kiwi", "Manzana", "naranja"]
print(id(fruits))
fruits_2 = fruits.copy()
print(id(fruits_2))

# 29. Copia una lista usando [:] y verifica que es una copia independiente.
fruits_3 = fruits[:]
print(id(fruits_3))

fruits_4 = list(fruits)
print(id(fruits_4))

# =====================================================
# SECCIÓN 8: Unir listas
# =====================================================

# 30. Une dos listas usando el operador `+`.
fruits = ["banana", "Kiwi", "Manzana", "naranja"]
vegetable = ["carrot", "broccoli",
             "spinach", "lettuce", "cucumber", "pepper"]

items_list = fruits + vegetable
print(items_list)

# 31. Usa un bucle for para añadir los elementos de una lista a otra.
for x in vegetable:
    fruits.append(x)

print(fruits)

# 32. Usa extend() para combinar dos listas.
fruits = ["banana", "Kiwi", "Manzana", "naranja", "Kiwi"]
vegetable = ["carrot", "broccoli",
             "spinach", "lettuce", "cucumber", "pepper"]
fruits.extend(vegetable)
print(fruits)

# =====================================================
# SECCIÓN 9: Métodos de listas
# =====================================================

# 33. Usa count() para saber cuántas veces aparece "carrot" en una lista.
vegetable = ["carrot", "broccoli",
             "spinach", "lettuce", "cucumber", "pepper", "carrot"]
print(vegetable.count("carrot"))

# 34. Usa index() para encontrar la posición de "Kiwi" en una lista.
fruits = ["banana", "Kiwi", "Manzana", "naranja", "Kiwi"]
print(fruits.index("Kiwi"))

# 35. Crea una lista, ordénala, luego invierte su orden con reverse().
fruits = ["banana", "Kiwi", "Manzana", "naranja"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

# 36. Crea una lista vacía y agrega elementos con append() y insert().
empty_list = list(())
empty_list.append("cherry")
print(empty_list)
empty_list.insert(1, "kiwi")
print(empty_list)

# 37. Usa pop() sin argumentos para eliminar el último elemento de una lista.
empty_list.pop()
print(empty_list)

# 38. Usa remove() para eliminar la primera ocurrencia de un valor repetido.
fruits = ["banana", "Kiwi", "Manzana", "naranja", "Kiwi", "carrot",
          "broccoli", "spinach", "lettuce", "cucumber", "pepper"]
fruits.remove("Kiwi")
print(fruits)

# 39. Usa clear() para vaciar completamente una lista y comprueba que está vacía con len().
fruits.clear()
print(len(fruits))
