# =====================================================
# 1. Almacenar estudiantes y sus calificaciones
# =====================================================
# Crea una lista de tuplas donde cada tupla contenga:
# (nombre_estudiante, [lista de calificaciones])
# Luego, muestra por cada estudiante:
# - Su nombre
# - Promedio
# - Si está aprobado (promedio >= 3)

# =====================================================
# 2. Agenda de contactos con búsqueda
# =====================================================
# Crea un diccionario donde la clave sea el nombre del contacto,
# y el valor sea una tupla con (teléfono, ciudad).
# Permite al usuario buscar un nombre y mostrar los datos correspondientes.

# =====================================================
# 3. Encuesta de hobbies
# =====================================================
# Crea un diccionario donde las claves son nombres y los valores son conjuntos con sus hobbies.
# Luego:
# - Muestra los hobbies únicos de todos los participantes.
# - Encuentra qué hobbies comparten al menos 2 personas.
# - Muestra los hobbies que no comparte nadie más.

# =====================================================
# 4. Análisis de palabras
# =====================================================
# Dado un texto de varias palabras en una lista:
# - Muestra cuántas palabras únicas hay (usa set).
# - Crea un diccionario con la palabra como clave y la cantidad de veces que aparece como valor.
# - Muestra la(s) palabra(s) más repetida(s).

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
