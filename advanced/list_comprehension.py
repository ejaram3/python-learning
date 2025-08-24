# Tema: List Comprehension y Funciones Lambda

"""
Descripción:
Permiten crear listas de forma concisa y declarar funciones pequeñas de forma rápida. 
- List comprehension: sintaxis compacta para crear listas a partir de iterables.
- Funciones lambda: funciones anónimas en una sola línea.
"""

# List Comprehension

lenguaje = "Python"
lista_1 = list(lenguaje)
print(lista_1)

lista_2 = [i for i in lenguaje]
print(lista_2)

lista_numeros = [n for n in range(6)]
print(lista_numeros)

cuadrados = [i * i for i in range(11)]
print(cuadrados)

lista_tuplas = [(i, i * i) for i in range(11)]
print(lista_tuplas)

pares = [i for i in range(21) if i % 2 == 0]
print(pares)

impares = [i for i in range(21) if i % 2 != 0]
print(impares)

numeros = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
pares_positivos = [i for i in numeros if i % 2 == 0 and i > 2]
print(pares_positivos)

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanamiento_lista = [numero for fila in lista_de_listas for numero in fila]
print(aplanamiento_lista)

# Funciones Lambda

suma_tradicional = lambda a, b: a + b
print(suma_tradicional(1, 3))

cuadrado_lambda = lambda x: x ** 2
print(cuadrado_lambda(3))

cubo_lambda = lambda x: x ** 3
print(cubo_lambda(3))

operacion_multiple = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(operacion_multiple(5, 5, 3))

def potencia(base):
    return lambda exponente: base ** exponente

print(potencia(2)(3))
print(potencia(2)(5))