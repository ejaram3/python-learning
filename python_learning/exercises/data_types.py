# =====================================================
# SECCIÓN 1: Identificación y creación de tipos de datos
# =====================================================

# 1. Crea una variable de cada uno de los siguientes tipos:
#    int, float, complex, str, list, tuple, dict, set, frozenset, bool, bytes, bytearray, memoryview, None
var_int = 23
var_float = 2.4
var_complex = 2j
var_string = "Hello"
var_list = ["grape", "apple", "orange"]
var_tuple = (0, 1, 0, 2)
var_dict = {"product": "car", "color": "red"}
var_frozenset = frozenset({"grape", "apple", "orange"})
var_bool = True
var_bytes = b"Hello"
var_bytearray = bytearray(8)
var_memoryview = memoryview(var_bytearray)
var_none = None

# 2. Imprime el tipo de cada variable usando la función type().
print(type(var_int))
print(type(var_float))
print(type(var_complex))
print(type(var_string))
print(type(var_list))
print(type(var_tuple))
print(type(var_dict))
print(type(var_frozenset))
print(type(var_bool))
print(type(var_bytes))
print(type(var_bytearray))
print(type(var_memoryview))
print(type(var_none))

# 3. Convierte una cadena "123" a entero y suma 10. Imprime el resultado.
value = int("123")
result = value + 10

# 4. Crea una lista con 5 elementos de distintos tipos de datos (por ejemplo: int, str, bool, etc.).
var_list = [23, "Hello", True, 2j, {"name": "elkin"}]

# 5. Crea una tupla con tres colores y accede al segundo color usando índices.
var_tuple = ("red", "green", "blue")
print(var_tuple[1])

# 6. Declara un diccionario con claves: "nombre", "edad", "ciudad", y asigna valores personalizados.
my_dict = {"name": "elkin", "age": 28, "city": "Soacha"}

# 7. Crea un conjunto (set) con al menos 3 frutas y agrega una fruta nueva.
my_set = {"Grape", "Orange", "Apple"}
my_set.add("Melon")

# 8. Declara una variable como `None` y luego cambia su valor por un número.
var_none = None
var_none = 1

# =====================================================
# SECCIÓN 2: Operaciones y manipulación
# =====================================================

# 9. Realiza las siguientes operaciones con dos variables numéricas:
#    suma, resta, multiplicación, división, división entera, módulo y exponente.
a = 7
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

# 10. Crea una cadena "Hola" y otra con tu nombre. Une ambas usando el operador + y muéstralo en mayúsculas.
greeting = "hello"
name = "Elkin"
result = greeting + " " + name
print(result.upper())

# 11. Crea una lista de números del 1 al 5. Usa append para agregar el número 6. Luego elimina el número 3.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(3)
print(numbers)

# 12. Crea un diccionario con productos y precios. Cambia el precio de un producto.
products = {
    "laptop": {"price": 450},
    "monitor": {"price": 150},
    "iphone": {"price": 780},
}
products["laptop"]["price"] = 400

print(products)

# 13. Usa un set para guardar los días de la semana. Agrega un duplicado y observa el resultado.
days_week = {
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo",
    "lunes",
}
print(days_week)

# 14. Usa una variable booleana para verificar si una persona es mayor de edad (edad >= 18).
age = 7
adult = True if age >= 18 else False

# 15. Convierte el número 45 a cadena y concaténalo con un mensaje: "Tienes X años".
age = str(45)
message = f"Tienes {age} años"
print(message)

# =====================================================
# SECCIÓN 3: Conversión de tipos
# =====================================================

# 16. Convierte un número flotante a entero y viceversa. Imprime ambos.
integer = 24
floating = 1.3
convert_integer = int(floating)
convert_floating = float(integer)
print(convert_integer)
print(convert_floating)

# 17. Convierte una lista en tupla, y una tupla en lista. Imprime los tipos antes y después.
list_1 = [23, "Hello", True, 2j, {"name": "elkin"}]
convert_tuple = tuple(list_1)
print(type(list_1))
print(type(convert_tuple))

# 18. Usa dict() para convertir una lista de pares en un diccionario: [("a", 1), ("b", 2)]
my_list = [("a", 1), ("b", 2)]
my_dict = dict(my_list)
print(my_dict)

# 19. Convierte una cadena a un conjunto de caracteres únicos.
phrase = "Hello word of python"
unique_characters = set(phrase)

# 20. Crea una cadena, codifícala a bytes con UTF-8 y luego decodifícala.
string = b"Hola mundo desde python"
text = string.decode("utf-8")
print(text)

# =====================================================
# SECCIÓN 4: Buenas prácticas y errores comunes
# =====================================================

# 21. Declara variables con nombres claros y en snake_case (ej: numero_total, nombre_usuario).
# first_name
# last_name

# 22. Intenta sumar un número y una cadena sin conversión. ¿Qué error ocurre?
# print('hello' + 1)

# 23. Intenta acceder a un índice inexistente en una lista. Captura la excepción con try/except.
my_list = [1, 2, 3, 4, 5]
try:
    print(my_list.index(10))
except ValueError:
    print(ValueError)

# 24. Declara un diccionario con claves repetidas. ¿Qué valor se guarda?
products = {
    "laptop": {"price": 450},
    "monitor": {"price": 150},
    "laptop": {"price": 780},
}
print(products)
# 25. Intenta modificar un valor dentro de una tupla. ¿Qué sucede?
my_tuple = ("red", "green", "blue")
# my_tuple[0] = 'white'

# =====================================================
# SECCIÓN 5: Mini desafíos prácticos
# =====================================================

# 26. Crea una función que reciba dos números y devuelva un diccionario con sus operaciones básicas (suma, resta, etc.).

# 27. Crea una lista con nombres. Convierte todos a mayúsculas usando un bucle.

# 28. Simula un carrito de compras usando un diccionario {producto: precio}, y calcula el total.

# 29. Crea un conjunto de cursos inscritos por un estudiante. Agrega uno nuevo y muestra cuántos cursos hay.

# 30. Crea un programa que reciba una lista de palabras y devuelva cuántas únicas hay (usa set).
