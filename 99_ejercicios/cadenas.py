# =====================================================
# Curso de Python - Ejercicios de Cadenas (Strings)
# =====================================================

"""
Cada sección contiene ejercicios prácticos relacionados con cadenas en Python.
Resuelve cada ejercicio debajo del comentario correspondiente.
Puedes ejecutar este archivo en cualquier editor.
"""

# =====================================================
# SECCIÓN 1: Sintaxis básica de strings
# =====================================================

# 1. Imprime la segunda letra de la cadena "Hola Mundo"
print("Hola Mundo"[1])

# 2. Crea una cadena multilínea y muestra cada línea por separado usando un bucle
string = """esta
es una
cadena de 
muchas 
lineas
"""
for line in string.split("\n"):
    print(line)

# 3. Cuenta cuántas veces aparece la letra "a" en una frase ingresada
phrase = "Hola mundo aprendiendo Python"
print(phrase.count("a"))


# 4. Función que devuelve True si la palabra contiene "python" (sin importar mayúsculas)
def search_word(phrase, word):
    if word.lower() in phrase.lower():
        answer = True
    else:
        answer = False
    return answer


print(search_word("Hola mundo desde Python", "PYTHON"))

# 5. Recorre la palabra "banana" e imprime cada letra en mayúscula
for letter in "banana":
    print(letter.upper())

# =====================================================
# SECCIÓN 2: Transformación de texto
# =====================================================

# 6. Convierte una frase a minúsculas, luego a mayúsculas, luego a formato título
phrase = "¡Hola mundo desde Python!"
print(phrase.lower())
print(phrase.upper())
print(phrase.title())


# 7. Función que recibe una cadena y devuelve el caso invertido (swapcase)
def invert_string(string):
    return string.swapcase()


print(invert_string(phrase))


# 8. Función que elimine tildes usando translate()
def remove_accents(phrase):
    return phrase.translate(str.maketrans("áéíóú", "aeiou"))


print(remove_accents("Búsqueda y verificación"))


# 9. Función que verifica si un texto está en minúsculas o mayúsculas
def is_upper_or_lower(text):
    if text.isupper():
        answer = "Texto en Mayúscula"
    elif text.islower():
        answer = "Texto en Minúscula"
    else:
        answer = "No definido"
    return answer


print(is_upper_or_lower("HOLA"))

# 10. Quita espacios sobrantes de "   hola mundo   " y aplícale title()
print("   hola mundo   ".strip().title())

# =====================================================
# SECCIÓN 3: Alineación de texto
# =====================================================

# 11. Muestra la palabra "Python" centrada en un campo de 20 caracteres con *
print("Python".center(20, "*"))

# 12. Alinea "42" a la derecha con ceros hasta ocupar 6 dígitos
print("42".rjust(6, "0"))

# 13. Alinea "hola" a la izquierda con guiones hasta 15 caracteres
print("hola".ljust(15, "-"))

# 14. Genera una tabla alineada de nombres y edades (usa ljust y rjust)
print("nombres".ljust(8, " "), "edades".rjust(8, " "))
print("Liseth".ljust(8, " "), "28".rjust(8, " "))
print("Elkin".ljust(8, " "), "27".rjust(8, " "))

# =====================================================
# SECCIÓN 4: Búsqueda y verificación
# =====================================================

# 15. Busca la palabra "python" en una cadena y muestra su posición si existe
print("Hola python".find("python"))

# 16. Encuentra la última aparición de la letra "a" usando rfind()
print("Hola aprendiendo python a tope".rfind("a"))

# 17. Usa .index() para buscar una palabra, controla el error si no existe
word = "tope"
try:
    string = "Hola aprendiendo python a tope"
    print(string.index(word))
except ValueError as err:
    print(err)

# 18. Verifica si una cadena empieza con "Hola" y termina con "adiós"
string = "Hola python, adiós"
print("True" if string.startswith("Hola") and string.endswith("adiós") else "False")

# 19. Cuenta cuántas veces aparece la letra "o" en un texto
print(string.count("o"))

# 20. Verifica si "nombre_1" es un identificador válido
print("nombre_1".isidentifier())

# =====================================================
# SECCIÓN 5: Separación y unión de texto
# =====================================================

# 21. Divide una frase en palabras usando split() y recórrelas una por una
phrase = "Hola mundo, aprendiendo Python"
for word in phrase.split(" "):
    print(word)

# 22. Une una lista de palabras con comas y un espacio con join()
list_words = ["Hola", "mundo", "desde", "Python"]
phrase_join = " ".join(list_words)
print(phrase_join)


# 23. Función que recibe "clave:valor" y lo separa con partition()
def separate_by_partition(string):
    result = string.partition(":")
    return result


print(separate_by_partition("nombre:Jose"))

# 24. Divide un texto multilínea con splitlines() y enuméralas
string = """esta
es una
cadena de 
muchas 
lineas
"""

for i, line in enumerate(string.splitlines()):
    print(i + 1, line)


# 25. Separa un archivo "documento.pdf" usando rpartition()
print("documento.pdf".rpartition("."))

# =====================================================
# SECCIÓN 6: Verificación de contenido
# =====================================================

# 26. Verifica si "Python3" es alfanumérico
print("Python3".isalnum())
# 27. Verifica si "SoloTexto" contiene solo letras
print("SoloTexto".isalpha())

# 28. Verifica si una cadena contiene solo espacios
print(" ".isspace())

# 29. Verifica si "123" es decimal, dígito y numérico
print("123".isdecimal())
print("123".isdigit())
print("123".isnumeric())


# 30. Verifica si "Mi Nombre Es Python" está en formato título
print("Mi Nombre Es Python".istitle())

# =====================================================
# SECCIÓN 7: Codificación, traducción y otros
# =====================================================

# 31. Codifica "Hola mundo" en utf-8 y luego decodifícalo
encode_string = "Hola mundo".encode("utf-8")
decode_string = encode_string.decode("utf-8")
print(encode_string)
print(decode_string)

# 32. Usa maketrans() y translate() para reemplazar vocales por números
print("Hola mundo aprendiendo Python".translate(str.maketrans("aeiou", "12345")))

# 33. Elimina las vocales de una frase usando translate()
print("Hola mundo aprendiendo Python".translate(str.maketrans("", "", "aeiouAEIOU")))

# 34. Reemplaza tabulaciones en "Nombre\tEdad" por 4 espacios con expandtabs()
print("Nombre\tEdad".expandtabs(4))


# 35. Función que recibe una cadena y la devuelve con swapcase()
def exchange_letters(phrase):
    return phrase.swapcase()


print(exchange_letters("Hola mundo desde Python"))
# =====================================================
# SECCIÓN 8: Proyecto Final - Procesador de Texto
# =====================================================

# 36. Crea una función llamada procesar_texto(texto) que:
# - Elimina espacios, tildes, y convierte a minúsculas
# - Cuenta cuántas veces aparece "python"
# - Reemplaza "python" por "🐍 Python"
# - Alinea la primera línea a la derecha
# - Devuelve un diccionario con la información procesada

# Escribe solo la estructura, no la solución. Resuélvelo paso a paso.

# def procesar_texto(texto):
#     # Paso 1: Limpieza
#     # Paso 2: Análisis
#     # Paso 3: Transformaciones
#     # Paso 4: Salida
#     pass
print("=" * 50)
text = """   ¡Hola! Me gusta Python.
Aprendí PYTHON con ejercicios.
Ahora uso Python todos los días.   """


def process_text(text):
    dict_summary = {}

    # Paso 1: Limpieza
    cleaning = text.strip().translate(str.maketrans("áéíóú", "aeiou")).lower()

    # Paso 2: Análisis
    analysis = cleaning.count("python")

    # Paso 3: Transformaciones
    transformations = cleaning.replace("python", "🐍 Python")
    transformations_by_lines = transformations.splitlines()
    align_first_line = transformations_by_lines[0].rjust(50)

    # Paso 4: Salida
    dict_summary["limpieza"] = cleaning
    dict_summary["analisis"] = analysis
    dict_summary["transformaciones"] = {
        "texto": transformations,
        "alineacion": align_first_line,
    }

    return dict_summary


print(process_text(text))
