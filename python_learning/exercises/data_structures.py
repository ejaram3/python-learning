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
    print(
        f"Nombre : {estudiante}\nPromedio: {promedio}\nEstado : {estado}\n{"-" * 20}")

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


print(buscar_en_agenda("felipe", agenda))

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

texto = ["Python", "es", "un", "lenguaje", "de", "programación", "Python", "es",
         "popular", "por", "su", "claridad", "de", "sintaxis", "y", "su", "comunidad",]

palabras_unicas = set(texto)
frecuencia = {}
for palabra in texto:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

top = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]

print(palabras_unicas)
print(frecuencia)
for item in top:
    palabra, posicion = item
    print((palabra, posicion))

# =====================================================
# 5. Catálogo de productos
# =====================================================
# Crea un diccionario de productos donde la clave sea el nombre del producto
# y el valor sea una tupla con (precio, stock).
# Luego:
# - Muestra todos los productos disponibles.
# - Permite al usuario “comprar” productos (restar al stock).
# - Si un producto queda en 0, márcalo como "agotado".

productos = {
    "Laptop": (1200, 2),
    "Smartphone": (800, 5),
    "Monitor": (450, 3),
    "Teclado": (50, 10),
    "Mouse": (25, 15),
    "Impresora": (300, 1),
    "Tablet": (600, 4),
    "Auriculares": (80, 12),
    "Cámara web": (150, 6),
    "Disco duro externo": (200, 3),
    "Altavoces": (120, 7),
    "Micrófono": (90, 5),
    "Silla ergonómica": (250, 2),
    "Router": (100, 8),
    "Memoria USB": (20, 0)
}

compra = input("Selecciona tu producto: ")
cantidad = int(input("Cantidad: "))

hay_producto = False

for producto, detalle in productos.items():
    if producto.lower() == compra.lower():
        hay_producto = True
        precio, stock = detalle
        if stock >= cantidad:
            nuevo_stock = stock - cantidad
            productos[producto] = (precio, nuevo_stock)
            total_pagar = precio * cantidad
            print(f"Producto: {producto}")
            print(f"Precio unitario: {precio}")
            print(f"Cantidad: {cantidad}")
            print(f"Total a pagar: {total_pagar}")
            print(f"Stock restante: {nuevo_stock}")
            if nuevo_stock < 1:
                print(f"Producto, {producto} agotado")
        else:
            print(f"No hay suficiente stock. Stock disponible: {stock}")

        break

if not hay_producto:
    print("El producto no existe.")

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

lista_1 = ["python", "java", "c++", "go", "kotlin"]
lista_2 = ["swift", "java", "go", "rust", "python"]
set_1 = set(lista_1)
set_2 = set(lista_2)

print(f"Elementos en común: {set_1.intersection(set_2)}")
print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}")
print(f"Union {set_1.union(set_2)}")

# =====================================================
# 7. Historial de visitas web
# =====================================================
# Crea una lista de diccionarios, cada uno representa una visita a un sitio:
# {"url": "...", "hora": "hh:mm", "usuario": "nombre"}
# Luego:
# - Muestra cuántas visitas hizo cada usuario (usa un dict de contadores).
# - Muestra todas las URLs únicas visitadas (usa set).
# - Encuentra el primer usuario que visitó "https://chat.openai.com".

visitas = [
    {"url": "https://chat.openai.com", "hora": "10:00", "usuario": "Ana"},
    {"url": "https://www.python.org", "hora": "10:05", "usuario": "Luis"},
    {"url": "https://chat.openai.com", "hora": "10:10", "usuario": "Luis"},
    {"url": "https://www.github.com", "hora": "10:15", "usuario": "Carlos"},
    {"url": "https://www.python.org", "hora": "10:20", "usuario": "Ana"},
    {"url": "https://www.stackoverflow.com", "hora": "10:25", "usuario": "Luis"}
]

# Contar visitas por usuario
contador_visitas = {}

for visita in visitas:
    usuario = visita["usuario"]
    contador_visitas[usuario] = contador_visitas.get(usuario, 0) + 1

print("Visitas por usuario:")
for usuario, cantidad in contador_visitas.items():
    print(f"{usuario}: {cantidad}")

# URLs únicas visitadas
urls_unicas = set()

for visita in visitas:
    urls_unicas.add(visita["url"])

print("\nURLs únicas visitadas:")
for url in urls_unicas:
    print(url)

# Primer usuario que visitó https://chat.openai.com
primer_usuario = None

for visita in visitas:
    if visita["url"] == "https://chat.openai.com":
        primer_usuario = visita["usuario"]
        break

if primer_usuario:
    print(
        f"\nEl primer usuario que visitó https://chat.openai.com fue: {primer_usuario}")
else:
    print("\nNadie visitó https://chat.openai.com")


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


libros = {
    1001: {
        "titulo": "La Odisea",
        "autor": "Homero",
        "año": "800",
        "categorias": ["aventura", "epica"]
    },
    1002: {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": "1605",
        "categorias": ["aventura", "ficcion", "clasico"]
    },
    1003: {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": "1967",
        "categorias": ["realismo magico", "ficcion"]
    },
    1004: {
        "titulo": "1984",
        "autor": "George Orwell",
        "año": "1949",
        "categorias": ["ficcion", "distopia", "politica"]
    },
    1005: {
        "titulo": "El gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "año": "1925",
        "categorias": ["drama", "clasico"]
    },
    1006: {
        "titulo": "El Código Da Vinci",
        "autor": "Dan Brown",
        "año": "2003",
        "categorias": ["misterio", "suspenso", "ficcion"]
    }
}

libros[1007] = {
    "titulo": "El nombre del viento",
    "autor": "Patrick Rothfuss",
    "año": "2011",
    "categorias": ["fantasia", "aventura"]
}

libros[1008] = {
    "titulo": "El marciano",
    "autor": "Andy Weir",
    "año": "2014",
    "categorias": ["ciencia ficcion", "supervivencia"]
}
libros[1009] = {
    "titulo": "La chica del tren",
    "autor": "Paula Hawkins",
    "año": "2015",
    "categorias": ["suspenso", "misterio"]
}

id_buscar = '1009'
autores = set()
despues_de_2010 = set()
libro = None

for id, detalle in libros.items():
    autores.add(detalle["autor"])

    if int(detalle["año"]) > 2010:
        despues_de_2010.add(detalle["titulo"])

    if int(id_buscar) == int(id):
        libro = detalle

print(f"Publicaciones después del año 2010:\n    {despues_de_2010}")
print(f"Autores únicos:\n    {autores}")

if libro:
    print(f"Resultado búsqueda:\n    {libro}")
else:
    print(f"Resultado búsqueda:\n    El id {id_buscar} no existe")


# =====================================================
# 9. Estudiantes por curso
# =====================================================
# Crea un diccionario donde las claves son nombres de cursos y los valores son conjuntos de estudiantes.
# Luego:
# - Muestra los estudiantes que están en ambos cursos "Python" y "Java".
# - Muestra los estudiantes que están solo en uno de los dos cursos.
# - Muestra todos los estudiantes únicos sin duplicados.

cursos = {
    "Python": {"Pedro", "José", "María", "Carlos"},
    "Java": {"Ana", "Luis", "Carlos"},
    "SQL": {"Sofía", "Pedro", "Elena"},
    "Git": {"José", "María", "Juan"},
    "HTML": {"Luis", "Carlos", "Elena"},
    "Django": {"Pedro", "Ana", "Sofía"},
    "Flask": {"María", "Juan", "Elena"},
    "C++": {"Carlos", "Luis", "José"},
    "React": {"Sofía", "Pedro", "Juan"},
    "Node": {"Ana", "María", "Carlos"}
}

curso_python = set()
curso_java = set()
estudiantes_unicos = set()

for curso, alumnos in cursos.items():
    estudiantes_unicos.update(alumnos)

    if curso == "Python":
        curso_python = alumnos
    elif curso == "Java":
        curso_java = alumnos

print(
    f"Alumnos en el curso de Java y Python: {curso_python.intersection(curso_java)}")
print(
    f"Alumnos en un solo curso Java o Python: {curso_python.symmetric_difference(curso_java)}")
print(f"Alumnos únicos en todos los cursos: {estudiantes_unicos}")

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

productos = [
    ("laptop", 5),
    ("mouse", 20),
    ("monitor", 7),
    ("teclado", 15),
    ("impresora", 3),
    ("tablet", 8),
    ("auriculares", 12),
    ("cámara web", 6),
    ("disco duro", 10),
    ("memoria usb", 25),
    ("router", 4),
    ("altavoces", 9),
    ("micrófono", 5),
    ("silla", 2),
    ("mochila", 14)
]
productos_dict = {}
for nombre, stock in productos:
    productos_dict[nombre] = stock

producto_buscar = 'tablet'
nuevo_stock = ""
eliminar = "si"  # "no"

producto_a_eliminar = None

for producto, stock in productos_dict.items():
    if producto_buscar == producto:
        if nuevo_stock != "":
            productos_dict[producto] = int(nuevo_stock)

        print(f"Producto: {producto}, Stock: {productos_dict[producto]}")

        if eliminar == "si":
            producto_a_eliminar = producto
        break


if producto_a_eliminar:
    del productos_dict[producto_a_eliminar]
    print(f"Producto {producto_a_eliminar} eliminado")

print(productos_dict)