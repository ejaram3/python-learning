# =====================================================
# Tema: Introducción a Python
# =====================================================

"""
Descripción:
Primera aproximación al lenguaje Python. Incluye historia breve, características clave,
instalación, uso de intérprete, y ejecución de scripts básicos.

Se cubre:
- Filosofía del lenguaje
- Primeros comandos
- Diferencias con otros lenguajes
"""

# =====================================================
# 1. Sintaxis básica
# =====================================================

# Comentarios:
# Esto es un comentario de una sola línea

"""
Este es un comentario
de múltiples líneas (en realidad es un string sin usar)
"""

# print() para mostrar resultados
print("Hola mundo")

# Asignación básica
x = 5
y = "Python"
print(x)
print(y)

# Tipado dinámico
x = 10      # entero
x = "Hola"  # ahora es string

# Case sensitive
nombre = "Elkin"
Nombre = "Otro"
print(nombre)
print(Nombre)

# =====================================================
# 2. Casos de uso comunes
# =====================================================

# Operaciones aritméticas
print(3 + 2)
print(10 / 2)
print(10 // 3)  # División entera
print(2 ** 3)   # Potencia

# Uso de input (comentado para evitar interrupciones en ejecución en lote)
# nombre = input("¿Cómo te llamas? ")
# print("Hola", nombre)

# Uso de variables sin declarar tipos explícitos
a = 10
b = 2.5
c = "texto"
d = True

# type() para verificar tipo de dato
print(type(a))
print(type(c))

# =====================================================
# 3. Buenas prácticas
# =====================================================

# - Usar nombres de variables descriptivos (ej: total_ventas en lugar de x)
# - Comentar código cuando la lógica no sea obvia
# - Escribir código limpio y con indentación clara (4 espacios)
# - Usar print() solo para debug o interacción básica

# =====================================================
# 4. Errores comunes
# =====================================================

# - Usar variables sin inicializar
# - Errores de indentación (espacios mal colocados)
# - Confundir = (asignación) con == (comparación)
# - Intentar usar input() sin entender que siempre devuelve string

# =====================================================
# 5. Recursos adicionales
# =====================================================

# - https://docs.python.org/3/tutorial/index.html
# - https://www.w3schools.com/python/
# - https://realpython.com/
