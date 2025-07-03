# =====================================================
# SECCIÓN 1: Creación y propiedades de los conjuntos
# =====================================================

# 1. Crea un conjunto con los elementos: "manzana", "banana", "cereza". Imprímelo.
frutas = {"manzana", "banana", "cereza"}
print(frutas)

# 2. Crea un conjunto que contenga elementos duplicados. Verifica que solo se almacenen una vez.
frutas = {"manzana", "banana", "cereza", "banana", "cereza"}
print(frutas)

# 3. Crea un conjunto mixto con datos de diferentes tipos (int, str, bool).
datos = {"Elkin", 27, True}

# 4. Crea un conjunto vacío y usa type() para confirmar que es un set.
vacio = set()
print(type(vacio))

# 5. Recorre un conjunto con un bucle `for` y muestra sus elementos uno por uno.
conjunto_1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{print(x) for x in conjunto_1}

# =====================================================
# SECCIÓN 2: Verificación y acceso
# =====================================================

# 6. Verifica si "pera" está en un conjunto. Imprime un mensaje adecuado.
frutas = {"manzana", "banana", "cereza", "banana", "pera"}
if "pera" in frutas:
    print("pera esta entre las frutas")

# 7. Verifica si un número NO está en el conjunto {1, 2, 3, 4, 5}.
numeros = {1, 2, 3, 4, 5}
if 10 not in numeros:
    print("10 no esta en la lista de numeros")

# =====================================================
# SECCIÓN 3: Agregar elementos
# =====================================================

# 8. Agrega "kiwi" a un conjunto de frutas usando add().
frutas = {"manzana", "banana", "cereza", "banana", "pera"}
frutas.add("kiwi")
print(frutas)

# 9. Agrega los elementos de otro conjunto al actual usando update().
frutas_citricas = {"naranja", "limón", "mandarina", "pomelo", "lima"}
frutas_tropicales = {"mango", "piña", "papaya", "guayaba", "maracuyá"}
frutas_citricas.update(frutas_tropicales)
print(frutas_citricas)

# 10. Agrega los elementos de una lista ["mango", "piña"] a un conjunto.
conjunto_frutas = {"naranja", "limón", "mandarina", "pomelo", "lima"}
lista_frutas = ["mango", "piña"]
conjunto_frutas.update(lista_frutas)
print(conjunto_frutas)

# =====================================================
# SECCIÓN 4: Eliminar elementos
# =====================================================

# 11. Crea un conjunto, elimina un elemento con remove() y muestra el resultado.
frutas = {'mango', 'piña', 'limón', 'pomelo', 'mandarina', 'lima', 'naranja'}
frutas.remove("mango")
print(frutas)

# 12. Usa discard() para intentar eliminar un elemento que no existe (sin lanzar error).
frutas = {'mango', 'piña', 'limón', 'pomelo', 'mandarina', 'lima', 'naranja'}
frutas.discard("uva")
print(frutas)

# 13. Usa pop() para eliminar un elemento aleatorio y muestra el resultado.
frutas = {'mango', 'piña', 'limón', 'pomelo', 'mandarina', 'lima', 'naranja'}
frutas.pop()
print(frutas)

# 14. Vacía un conjunto con clear() y verifica que está vacío.
frutas = {'mango', 'piña', 'limón', 'pomelo', 'mandarina', 'lima', 'naranja'}
frutas.clear()
print(frutas)

# =====================================================
# SECCIÓN 5: Operaciones entre conjuntos
# =====================================================

# 15. Declara dos conjuntos y obtén su unión usando union() y |.
a = {"a", "b", "c"}
b = {1, 2, 3}
u1 = a.union(b)
print(u1)

u2 = b | a
print(u2)

# 16. Declara dos conjuntos y obtén su intersección usando intersection() y &.
a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "o"}
i1 = a.intersection(b)
print(i1)

i2 = a & b
print(i2)

# 17. Declara dos conjuntos y obtén su diferencia (elementos solo en el primero).
a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "o"}
d1 = a.difference(b)
print(d1)

d2 = a - b
print(d2)

# 18. Declara dos conjuntos y obtén la diferencia simétrica.
a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "u"}
ds1 = a.symmetric_difference(b)
print(ds1)

ds2 = a ^ b
print(ds2)

# 19. Usa intersection_update() para modificar el primer conjunto con los valores comunes.
a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "u"}
a.intersection_update(b)
print(a)

# 20. Usa difference_update() para quitar del primer conjunto los elementos del segundo.
a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "u"}
a.difference_update(b)
print(a)

# 21. Usa symmetric_difference_update() para modificar el primer conjunto con los elementos únicos.
a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "u"}
a.symmetric_difference_update(b)
print(a)

# =====================================================
# SECCIÓN 6: Métodos lógicos de conjuntos
# =====================================================

# 22. Usa isdisjoint() para verificar si dos conjuntos no comparten elementos.
print(a.isdisjoint(b))

# 23. Usa issubset() para comprobar si un conjunto está contenido en otro.
print(a.issubset(b))

# 24. Usa issuperset() para comprobar si un conjunto contiene a otro completamente.
print(a.issuperset(b))

# =====================================================
# SECCIÓN 7: Aplicaciones prácticas
# =====================================================

# 25. Crea dos listas con datos repetidos, conviértelas en conjuntos y muestra los elementos únicos.
lista_frutas_1 = ["manzana", "pera", "manzana", "uva", "pera"]
lista_frutas_2 = ["kiwi", "banana", "kiwi", "banana", "mango"]

frutas_unicas = set(set(lista_frutas_1).union(set(lista_frutas_2)))
print(frutas_unicas)

# 26. Crea un conjunto de usuarios registrados y verifica si un nuevo usuario ya existe antes de agregarlo.
usuarios = {"juan23", "ana_lpz", "carlos88", "maria99"}

usuario = "juan2"
if usuario not in usuarios:
    usuarios.add(usuario)

print(usuarios)

# 27. Simula una encuesta: crea un conjunto con frutas preferidas de diferentes personas. Usa union() para obtener la lista total sin duplicados.
# Listas individuales por persona encuestada
persona_1 = {"mango", "fresa", "mango"}
persona_2 = {"manzana", "pera", "manzana"}
persona_3 = {"sandía", "piña", "mango"}
persona_4 = {"mango", "uva", "fresa"}
persona_5 = {"kiwi", "fresa", "fresa", "banano"}
persona_6 = {"banano", "piña", "mango"}

resultado_encuesta = persona_1 | persona_2 | persona_3 | persona_4 | persona_5 | persona_6
print(resultado_encuesta)

# 28. Dado un conjunto de palabras, elimina todas las que empiezan por vocal (usa comprensión de conjuntos si quieres un reto).
palabras_mixtas = {"avión", "elefante", "iguana", "oruga",
                   "uva", "perro", "gato", "ratón", "lobo", "tigre"}

palabras_filtradas = {x for x in palabras_mixtas if not (
    x.lower().startswith(("a", "e", "i", "o", "u")))}

print(palabras_filtradas)

# 29. Crea una función que reciba dos conjuntos y retorne un diccionario con:
#     - su unión
#     - su intersección
#     - su diferencia
#     - su diferencia simétrica


def operacion_conjuntos(conjunto1, conjunto2):
    return {"Union": conjunto1 | conjunto2,
            "Interseccion": conjunto1 & conjunto2,
            "Diferencia": conjunto1 - conjunto2,
            "Diferencia simetrica": conjunto1 ^ conjunto2}


a = {"a", "b", "c", "e"}
b = {"a", "e", "i", "o", "u"}

print(operacion_conjuntos(a, b))

# 30. Dado un conjunto de números del 1 al 10, elimina todos los pares usando un bucle.
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_filtrados = {n for n in numeros if not (n % 2 == 0)}
print(numeros_filtrados)
