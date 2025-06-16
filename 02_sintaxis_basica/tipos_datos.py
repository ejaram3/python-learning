# =====================================================
# Tema: Tipos de Datos en Python
# =====================================================

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

# =====================================================
# 1. Sintaxis básica
# =====================================================

# Números
entero = 10  # int
flotante = 10.5  # float
complejo = 3 + 4j  # complex

# Secuencias
cadena = "Hola, mundo"  # str
lista = [1, 2, 3]  # list
tupla = (1, 2, 3)  # tuple
rango = range(5)  # range

# Mapeo
diccionario = {"nombre": "Elkin", "edad": 28}  # dict

# Conjuntos
conjunto = {1, 2, 3}  # set
conjunto_inmutable = frozenset({1, 2, 3})  # frozenset

# Booleanos
verdadero = True  # bool
falso = False  # bool

# Binarios
bytes_datos = b"Hola"  # bytes
bytearray_datos = bytearray(5)  # bytearray
memoria = memoryview(bytes(5))  # memoryview

# Especial
nulo = None  # NoneType

# Verificación de tipos
print(type(entero))
print(type(cadena))
print(type(diccionario))

# =====================================================
# 2. Casos de uso comunes
# =====================================================

# Operaciones numéricas
a = 10
b = 3
print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División
print(a % b)  # Módulo
print(a ** b)  # Exponenciación
print(a // b)  # División entera

# Manipulación de cadenas
saludo = "Hola"
nombre = "Elkin"
mensaje = saludo + " " + nombre
print(mensaje)
print(mensaje.upper())
print(mensaje.lower())
print(mensaje.replace("Elkin", "Mundo"))

# Listas
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)
print(numeros[2])

# Diccionarios
persona = {"nombre": "Elkin", "edad": 28}
print(persona["nombre"])
persona["edad"] = 29
print(persona)

# Conjuntos
frutas = {"manzana", "banana", "cereza"}
frutas.add("naranja")
print(frutas)

# Booleanos
x = 5
y = 10
print(x > y)
print(x < y)

# Conversión de tipos
numero_str = "100"
numero_int = int(numero_str)
print(numero_int + 50)

# =====================================================
# 3. Buenas prácticas
# =====================================================

# - Usar nombres de variables descriptivos y en snake_case.
# - Inicializar variables antes de usarlas.
# - Evitar sobrescribir nombres de funciones o palabras reservadas.
# - Comentar el código para mejorar la legibilidad.
# - Utilizar funciones y estructuras de control para evitar la repetición.

# =====================================================
# 4. Errores comunes
# =====================================================

# - Usar variables sin inicializarlas.
# - Confundir tipos al operar (ej. sumar str con int).
# - Modificar tipos inmutables.
# - Duplicar claves en diccionarios.
# - Índices fuera de rango.

# =====================================================
# 5. Recursos adicionales
# =====================================================

# - https://docs.python.org/3/library/stdtypes.html
# - https://www.w3schools.com/python/python_datatypes.asp
# - https://www.geeksforgeeks.org/python-data-types/