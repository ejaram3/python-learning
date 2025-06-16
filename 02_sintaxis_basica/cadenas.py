# =====================================================
# Tema: Strings
# =====================================================

"""
Descripción:
Las cadenas en Python se definen usando comillas simples o dobles.
Se pueden usar comillas dentro de cadenas, siempre que no coincidan con las que rodean la cadena.
Incluye todos los métodos oficiales de str con ejemplos y comentarios.
"""

# =====================================================
# 1. Sintaxis básica
# =====================================================

print("It's alright")  # Comillas internas válidas
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hola"
print(a)

a = '''Esta
es una
cadena
de multiples
lineas'''
print(a)

a = "Hola mundo!"
print(a[1])

for x in "banana":
    print(x)

print(len(a))

print("free" in a)
if "free" in a:
    print("Sí, 'free' está presente")
if "expensive" not in a:
    print("No, 'expensive' NO está presente")

# =====================================================
# 2. Casos de uso comunes y métodos de str
# =====================================================

# Métodos de transformación
print("hola mundo".capitalize())       # Primera letra en mayúscula
print("Hola Bienvenido".casefold())    # Minúsculas para comparaciones seguras
print("Python".lower())                # Todo a minúsculas
print("python".upper())                # Todo a mayúsculas
print("   texto   ".strip())           # Quita espacios al inicio y final
print("   texto".lstrip())             # Quita espacios a la izquierda
print("texto   ".rstrip())             # Quita espacios a la derecha
print("Hola mundo".replace("mundo", "Python"))  # Reemplazo
print("Hola mundo".swapcase())         # Cambia mayúsculas ↔ minúsculas
print("hola mundo".title())            # Formato Título

# Métodos de alineación
print("Python".center(10, "-"))         # Centrado con relleno
print("Python".ljust(10, "-"))          # Izquierda con relleno
print("Python".rjust(10, "-"))          # Derecha con relleno
print("42".zfill(6))                    # Relleno con ceros a la izquierda

# Métodos de búsqueda y validación
print("Python es genial".find("genial"))    # Índice de subcadena o -1
print("Python es genial".rfind("o"))        # Última aparición de subcadena
print("Python es genial".index("genial"))   # Índice o error si no existe
print("Python es genial".rindex("o"))       # Último índice o error
print("archivo.txt".startswith("archivo"))  # Inicia con...
print("archivo.txt".endswith(".txt"))        # Termina con...

# Métodos de separación y unión
print("a,b,c".split(","))                # Divide por comas
print("a,b,c".rsplit(","))               # Divide desde la derecha
print("línea1\nlínea2\nlínea3".splitlines())  # Divide por saltos de línea
print("nombre:edad:ciudad".partition(":"))    # Divide en 3 (izq, sep, der)
print("nombre:edad:ciudad".rpartition(":"))   # Igual pero desde la derecha
print(", ".join(["Python", "es", "genial"])) # Une lista con separador

# Métodos de verificación booleana
print("Texto123".isalnum())       # Alfanumérico
print("Texto".isalpha())          # Solo letras
print("123".isdecimal())          # Solo dígitos decimales
print("123".isdigit())            # Solo dígitos
print("½".isnumeric())            # Numérico extendido
print("   ".isspace())            # Solo espacios
print("variable".isidentifier())  # Nombre válido de variable
print("todo en minúsculas".islower())  # Todo minúscula
print("TODO EN MAYÚSCULAS".isupper())  # Todo mayúscula
print("Título Correcto".istitle())     # Formato título
print("Texto visible".isprintable())   # Todos los caracteres imprimibles
print("ASCII".isascii())               # Todos los caracteres son ASCII

# Métodos de codificación y traducción
print("Hola mundo".encode("utf-8"))     # Codifica a bytes
print("Nombre\tEdad".expandtabs(4))     # Reemplaza \t por espacios
tabla = str.maketrans("aeiou", "12345")
print("hola mundo".translate(tabla))    # Reemplaza usando tabla

# =====================================================
# 3. Buenas prácticas
# =====================================================

# - Usar f-strings en lugar de concatenaciones clásicas.
# - Validar substrings con 'in' antes de usar index().
# - Usar métodos como strip(), replace(), lower() al procesar texto.
# - Aprovechar join() para unir estructuras con separadores.

# =====================================================
# 4. Errores comunes
# =====================================================

# - Usar index() sin validar presencia puede lanzar ValueError.
# - No tener en cuenta que las strings son inmutables.
# - Confundir isdigit() con isnumeric() (este último acepta más símbolos).
# - No eliminar espacios invisibles antes de comparar strings.

# =====================================================
# 5. Recursos adicionales
# =====================================================

# - https://docs.python.org/3/library/stdtypes.html#string-methods
# - https://www.w3schools.com/python/python_strings_methods.asp