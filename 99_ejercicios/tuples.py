# =====================================================
# SECCIÓN 1: Creación y sintaxis básica
# =====================================================

# 1. Crea una tupla con los nombres de 3 ciudades y muéstrala.
import math
ciudades = ("Bogota", "Paris", "Londres")
print(ciudades)

# 2. Crea una tupla que contenga un solo elemento ("python",). Imprime su tipo para verificar.
elemento = ("python",)
print(type(elemento))

# 3. Crea una tupla con elementos repetidos y muestra cuántos elementos tiene con len().
frutas = ("manzana", "pera", "uva", "naranja", "uva", "pera", "manzana")
print(len(frutas))

# 4. Crea una tupla utilizando el constructor tuple() a partir de una lista.
frutas = ["manzana", "pera", "uva", "naranja", "uva", "pera", "manzana"]
tupla_frutas = list(frutas)

# =====================================================
# SECCIÓN 2: Acceso y slicing
# =====================================================

# 5. Crea una tupla de frutas y muestra el primer y último elemento.
frutas = ("manzana", "pera", "uva", "naranja", "uva", "pera")
print(frutas[0])
print(frutas[-1])

# 6. Accede a los elementos del índice 1 al 3 en una tupla de al menos 5 elementos.
print(frutas[0:3])

# 7. Verifica si "banana" existe dentro de una tupla.
print("banana" in frutas)

# 8. Usa slicing para obtener:
#    a) Los 3 primeros elementos
#    b) Todos los elementos desde el índice 2
#    c) Los dos últimos elementos con índices negativos
print(frutas[:3])
print(frutas[2:])
print(frutas[-2:])

# =====================================================
# SECCIÓN 3: Inmutabilidad y soluciones
# =====================================================

# 9. Crea una tupla, conviértela a lista, cambia un valor, y vuelve a convertirla en tupla.
lenguajes_programacion = tuple(("Python", "Java", "C", "C++", "JavaScript", "Go", "Rust", "Ruby", "Kotlin",
                               "Swift", "TypeScript", "PHP", "Perl", "Scala", "R", "MATLAB", "Dart", "Haskell", "Elixir", "Lua"))
lista = list(lenguajes_programacion)
lista[19] = "C#"
lenguajes_programacion = tuple(lista)
print(lenguajes_programacion)

# 10. Agrega un elemento a una tupla (usando conversión a lista).
lenguajes_programacion = list(lista)
lista.append("Lua")
lenguajes_programacion = tuple(lista)
print(lenguajes_programacion)

# 11. Elimina un elemento de una tupla (conviértela a lista y luego a tupla).
lista = list(lenguajes_programacion)
lista.remove("MATLAB")
lenguajes_programacion = tuple(lista)
print(lenguajes_programacion)

# 12. Une dos tuplas diferentes y guarda el resultado en una nueva tupla.
marca_carros = tuple(("Toyota", "BMW", "Ford", "Kia"))
marca_aviones = tuple(("Boeing", "Airbus", "Embraer", "Bombardier"))
marca_carros += marca_aviones
print(marca_carros)

# 13. Repite una tupla de 2 elementos, 3 veces.
marca = tuple(('Kia', 'Boeing'))
print(marca * 3)

# =====================================================
# SECCIÓN 4: Desempaquetado de tuplas
# =====================================================

# 14. Desempaqueta una tupla de 3 colores en 3 variables distintas.
colores = tuple(("rojo", "negro", "blanco"))
rojo, negro, blanco = colores
print(rojo)
print(negro)
print(blanco)

# 15. Usa el operador * para capturar múltiples elementos del medio de una tupla.
lenguajes = tuple(("Python", "Java", "C", "C++", "JavaScript", "Go", "Rust", "Ruby", "Kotlin",
                   "Swift", "TypeScript", "PHP", "Perl", "Scala", "R", "MATLAB", "Dart", "Haskell", "Elixir", "Lua"))
favorito, *otros = lenguajes
print(favorito)
print(otros)

# 16. Desempaqueta una tupla de 5 elementos de forma que el primero y el último queden separados, y el resto agrupado en una lista.
lenguajes = tuple(("Python", "Java", "C", "C++", "JavaScript"))
favorito, *otros, no_gusta = lenguajes
print(favorito)
print(otros)
print(no_gusta)

# =====================================================
# SECCIÓN 5: Recorrido de tuplas
# =====================================================

# 17. Recorre una tupla con un bucle for e imprime cada elemento.
lenguajes = tuple(("Python", "Java", "C", "C++", "JavaScript", "Go", "Rust", "Ruby", "Kotlin",
                   "Swift", "TypeScript", "PHP", "Perl", "Scala", "R", "MATLAB", "Dart", "Haskell", "Elixir", "Lua"))
for lenguaje in lenguajes:
    # print(lenguaje)
    pass

# 18. Recorre una tupla usando un índice (for + range).
for l in range(len(lenguajes)):
    # print(lenguajes[l])
    pass

# 19. Recorre una tupla con un bucle while.
lenguaje = 0
while lenguaje < len(lenguajes):
    print(lenguajes[lenguaje])
    lenguaje += 1

# =====================================================
# SECCIÓN 6: Métodos de tuplas
# =====================================================

# 20. Usa count() para saber cuántas veces aparece "python" en una tupla.
lenguajes = tuple(("Python", "Java", "C", "C++", "JavaScript", "Go", "Rust", "Ruby", "Kotlin",
                   "Swift", "TypeScript", "PHP", "Perl", "Scala", "R", "MATLAB", "Dart", "Haskell", "Elixir", "Lua"))
print(lenguajes.count("Python"))

# 21. Usa index() para encontrar la posición de "Go" en una tupla.
print(lenguajes.index("Go"))

# =====================================================
# SECCIÓN 7: Aplicaciones prácticas
# =====================================================

# 22. Crea una función que reciba una tupla de números y devuelva:
#     - La suma de sus elementos
#     - El promedio


def suma_numeros(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio


numeros = tuple((1, 3, 4, 4, 6, 7))
suma, promedio = suma_numeros(numeros)
print(f"Suma: {suma}\nPromedio: {promedio:.2f}")

# 23. Crea una tupla que represente un producto (nombre, precio, cantidad) y muestra la información formateada con f-string.
producto = tuple(("KIA", 45.213244, 1))
marca, precio, cantidad = producto
print(f"Marca: {marca}\nPrecio: {precio:.2f}\nCantidad: {cantidad}")

# 24. Simula coordenadas cartesianas usando tuplas: (x, y). Declara 3 puntos y calcula distancias básicas entre ellos.

# Coordenadas (x, y) de los puntos
A = (1, 2)
B = (4, 5)
C = (6, 1)


def distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


d_AB = distancia(A, B)
d_BC = distancia(B, C)
distancia_total = d_AB + d_BC

print(f"Distancia A→B: {d_AB:.2f}")
print(f"Distancia B→C: {d_BC:.2f}")
print(f"Distancia total A→B→C: {distancia_total:.2f}")


# 25. Dada una tupla de nombres, crea una nueva tupla con todos los nombres en mayúsculas.
nombres = tuple(("Carlos", "Ana", "Luis", "María", "Jorge",
                "Lucía", "Andrés", "Valentina", "Pedro", "Camila"))
nombres = tuple(list(nombre.upper() for nombre in nombres))
print(nombres)
