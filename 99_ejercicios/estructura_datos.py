# =====================================================
# 1. Almacenar estudiantes y sus calificaciones
# =====================================================
# Crea una lista de tuplas donde cada tupla contenga:
# (nombre_estudiante, [lista de calificaciones])
# Luego, muestra por cada estudiante:
# - Su nombre
# - Promedio
# - Si está aprobado (promedio >= 3)
calificaciones = [
    ("Ana", [4.5, 4.8, 5.0, 4.2, 4.7]),
    ("Carlos", [3.8, 3.2, 4.0, 2.9, 3.5]),
    ("Sofía", [5.0, 4.9, 4.8, 5.0, 4.9]),
    ("David", [2.9, 3.1, 2.5, 3.0, 2.2]),
    ("Valentina", [4.2, 4.0, 3.8, 4.5, 4.1]),
    ("Mateo", [3.5, 3.6, 3.7, 3.4, 3.5]),
    ("Camila", [4.9, 4.7, 5.0, 4.8, 4.9]),
    ("Santiago", [3.1, 2.8, 3.5, 3.0, 3.2]),
    ("Isabella", [4.7, 4.6, 4.8, 4.5, 4.9]),
    ("Andrés", [2.5, 3.0, 2.2, 1.9, 2.8]),
    ("Laura", [3.9, 4.1, 4.0, 3.8, 4.2]),
    ("Juan", [1.8, 2.5, 3.0, 1.5, 2.1]),
    ("Gabriela", [4.0, 4.3, 3.7, 4.1, 4.5]),
    ("Luis", [2.2, 2.0, 1.8, 2.5, 2.3]),
]

for estudiante, notas in calificaciones:
    promedio = sum(notas) / len(notas)
    estado = "Aprobado" if promedio >= 3 else "No aprobado"
    # print(f"Nombre : {estudiante}\nPromedio: {promedio}\nEstado : {estado}\n{"-" *20}")

# =====================================================
# 2. Agenda de contactos con búsqueda
# =====================================================
# Crea un diccionario donde la clave sea el nombre del contacto,
# y el valor sea una tupla con (teléfono, ciudad).
# Permite al usuario buscar un nombre y mostrar los datos correspondientes.
agenda = {
    "Elkin": (3126543289, "Bogotá"),
    "Laura": (3109876543, "Medellín"),
    "Carlos": (3112233445, "Cali"),
    "Andrea": (3133344556, "Barranquilla"),
    "Felipe": (3151122334, "Bucaramanga"),
    "Diana": (3164455667, "Manizales"),
}


def buscar_en_agenda(contacto: str, agenda: dict):
    nombre = contacto.title()
    if nombre in agenda:
        telefono, ciudad = agenda[nombre]
        return f"Nombre: {nombre}\nTelefono: {telefono}\nCiudad: {ciudad}"
    else:
        return f"{nombre} no está en la agenda."


# print(buscar_en_agenda("felipe", agenda))

# =====================================================
# 3. Encuesta de hobbies
# =====================================================
# Crea un diccionario donde las claves son nombres y los valores son conjuntos con sus hobbies.
# Luego:
# - Muestra los hobbies únicos de todos los participantes.
# - Encuentra qué hobbies comparten al menos 2 personas.
# - Muestra los hobbies que no comparte nadie más.

hobbies_personas = {
    "Elkin": {"leer", "ver películas", "jugar", "programar"},
    "Valentina": {"bailar", "leer", "viajar", "jugar", "ver películas"},
    "Samuel": {"programar", "hacer ejercicio", "ver películas", "leer"},
    "Camila": {"viajar", "ver series", "cocinar"},
    "Andrés": {"ver películas", "fotografía", "andar en bicicleta"},
    "Isabela": {"leer", "dibujar", "viajar", "ver películas"},
}

contador_hobbies = {}
todos_hobbies = []

for hobbies in hobbies_personas.values():
    for hobby in hobbies:
        todos_hobbies.append(hobby)
        if hobby in contador_hobbies:
            contador_hobbies[hobby] += 1
        else:
            contador_hobbies[hobby] = 1

hobbies_duplicados = {
    hobby for hobby, cantidad in contador_hobbies.items() if cantidad > 1
}
hobbies_unicos = set(todos_hobbies)

hobbies_no_comparten = {
    hobby for hobby, cantidad in contador_hobbies.items() if cantidad == 1
}

print(f"Hobbies duplicados:\n    {hobbies_duplicados}")
print(f"Hobbies únicos:\n    {hobbies_unicos}")
print(f"Hobbies no compartidos:\n    {hobbies_no_comparten}")

# =====================================================
# 4. Análisis de palabras
# =====================================================
# Dado un texto de varias palabras en una lista:
# - Muestra cuántas palabras únicas hay (usa set).
# - Crea un diccionario con la palabra como clave y la cantidad de veces que aparece como valor.
# - Muestra la(s) palabra(s) más repetida(s).

texto = [
    "Python", "es", "un", "lenguaje", "de", "programación", "Python", "es", "popular", 
    "por", "su", "claridad", "de", "sintaxis", "y", "su", "comunidad"
]

# =====================================================
# 5. Catálogo de productos
# =====================================================
# Crea un diccionario de productos donde la clave sea el nombre del producto
# y el valor sea una tupla con (precio, stock).
# Luego:
# - Muestra todos los productos disponibles.
# - Permite al usuario “comprar” productos (restar al stock).
# - Si un producto queda en 0, márcalo como "agotado".

# =====================================================
# 6. Intersección de datos
# =====================================================
# Dado dos listas:
# - lista_1 = ["python", "java", "c++", "go", "kotlin"]
# - lista_2 = ["swift", "java", "go", "rust", "python"]
# Realiza:
# - Los elementos que están en ambas (intersección)
# - Los elementos que están solo en una (diferencia simétrica)
# - Todos los elementos sin repetir (unión)

# =====================================================
# 7. Historial de visitas web
# =====================================================
# Crea una lista de diccionarios, cada uno representa una visita a un sitio:
# {"url": "...", "hora": "hh:mm", "usuario": "nombre"}
# Luego:
# - Muestra cuántas visitas hizo cada usuario (usa un dict de contadores).
# - Muestra todas las URLs únicas visitadas (usa set).
# - Encuentra el primer usuario que visitó "https://chat.openai.com".

# =====================================================
# 8. Base de datos de libros
# =====================================================
# Crea un diccionario donde cada clave es un ID de libro (entero),
# y el valor es otro diccionario con: título, autor, año, y categorías (como lista).
# Luego:
# - Agrega 3 libros a la base.
# - Muestra los títulos publicados después del año 2010.
# - Muestra todos los autores únicos (usa set).
# - Permite buscar un libro por ID y mostrar toda su información.

# =====================================================
# 9. Estudiantes por curso
# =====================================================
# Crea un diccionario donde las claves son nombres de cursos y los valores son conjuntos de estudiantes.
# Luego:
# - Muestra los estudiantes que están en ambos cursos "Python" y "Java".
# - Muestra los estudiantes que están solo en uno de los dos cursos.
# - Muestra todos los estudiantes únicos sin duplicados.

# =====================================================
# 10. Inventario de una tienda
# =====================================================
# Usa una lista de tuplas para representar productos en el inventario:
# [("laptop", 5), ("mouse", 20), ("monitor", 7), ...]
# Luego convierte esta estructura en un diccionario donde la clave sea el nombre del producto
# y el valor sea el stock. Permite:
# - Consultar el stock de un producto.
# - Actualizar el stock de un producto.
# - Eliminar un producto del inventario.
