# Tema: Tipos de Datos en Python

"""
Descripción:
Los tipos de datos en Python definen la naturaleza de los valores que pueden ser almacenados y manipulados. Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de una variable explícitamente; el intérprete lo determina en tiempo de ejecución.

Los tipos de datos incorporados en Python se clasifican en las siguientes categorías:
- Numéricos: int, float, complex
- Secuencias: str, list, tuple, range
- Mapeos: dict
- Conjuntos: set, frozenset
- Booleanos: bool
- Binarios: bytes, bytearray, memoryview
- Especiales: NoneType

Cada tipo de dato tiene características y métodos específicos que permiten realizar operaciones particulares.
"""

# Sintaxis básica

entero = 10
flotante = 10.5
complejo = 3 + 4j

cadena = "Hola, mundo"
lista = [1, 2, 3]
tupla = (1, 2, 3)
rango = range(5)

diccionario = {"nombre": "Elkin", "edad": 28}

conjunto = {1, 2, 3}
conjunto_inmutable = frozenset({1, 2, 3})

verdadero = True
falso = False

bytes_datos = b"Hola"
bytearray_datos = bytearray(5)
memoria = memoryview(bytes(5))

nulo = None

print(type(entero))
print(type(cadena))
print(type(diccionario))

# Casos de uso comunes

a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

saludo = "Hola"
nombre = "Elkin"
mensaje = saludo + " " + nombre
print(mensaje)
print(mensaje.upper())
print(mensaje.lower())
print(mensaje.replace("Elkin", "Mundo"))

numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)
print(numeros[2])

persona = {"nombre": "Elkin", "edad": 28}
print(persona["nombre"])
persona["edad"] = 29
print(persona)

frutas = {"manzana", "banana", "cereza"}
frutas.add("naranja")
print(frutas)

x = 5
y = 10
print(x > y)
print(x < y)

numero_str = "100"
numero_int = int(numero_str)
print(numero_int + 50)
