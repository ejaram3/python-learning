# Tema: Strings

"""
Descripción:
Las cadenas en Python se definen usando comillas simples o dobles.
Se pueden usar comillas dentro de cadenas, siempre que no coincidan con las que rodean la cadena.
Incluye todos los métodos oficiales de str con ejemplos y comentarios.
"""

# Sintaxis básica

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

saludo = "Hola"
print(saludo)

multi_linea = '''Esta
es una
cadena
de multiples
lineas'''
print(multi_linea)

mensaje = "Hola mundo!"
print(mensaje[1])

for letra in "banana":
    print(letra)

print(len(mensaje))

print("free" in mensaje)
if "free" in mensaje:
    print("Sí, 'free' está presente")
if "expensive" not in mensaje:
    print("No, 'expensive' NO está presente")

# Casos de uso comunes y métodos de str

# Transformación
print("hola mundo".capitalize())
print("Hola Bienvenido".casefold())
print("Python".lower())
print("python".upper())
print("   texto   ".strip())
print("   texto".lstrip())
print("texto   ".rstrip())
print("Hola mundo".replace("mundo", "Python"))
print("Hola mundo".swapcase())
print("hola mundo".title())

# Alineación
print("Python".center(10, "-"))
print("Python".ljust(10, "-"))
print("Python".rjust(10, "-"))
print("42".zfill(6))

# Búsqueda y validación
print("Python es genial".find("genial"))
print("Python es genial".rfind("o"))
print("Python es genial".index("genial"))
print("Python es genial".rindex("o"))
print("archivo.txt".startswith("archivo"))
print("archivo.txt".endswith(".txt"))

# Separación y unión
print("a,b,c".split(","))
print("a,b,c".rsplit(","))
print("línea1\nlínea2\nlínea3".splitlines())
print("nombre:edad:ciudad".partition(":"))
print("nombre:edad:ciudad".rpartition(":"))
print(", ".join(["Python", "es", "genial"]))

# Verificación booleana
print("Texto123".isalnum())
print("Texto".isalpha())
print("123".isdecimal())
print("123".isdigit())
print("\u00bd".isnumeric())
print("   ".isspace())
print("variable".isidentifier())
print("todo en minúsculas".islower())
print("TODO EN MAYÚSCULAS".isupper())
print("Título Correcto".istitle())
print("Texto visible".isprintable())
print("ASCII".isascii())

# Codificación y traducción
print("Hola mundo".encode("utf-8"))
print("Nombre\tEdad".expandtabs(4))
tabla_traduccion = str.maketrans("aeiou", "12345")
print("hola mundo".translate(tabla_traduccion))
