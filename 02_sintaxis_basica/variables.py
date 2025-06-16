# =====================================================
# Tema: Variables
# =====================================================

"""
Descripción:
Las variables en Python son espacios en memoria usados para guardar datos.
No requieren declaración explícita de tipo debido a que Python es un lenguaje de tipado dinámico.
Se utilizan para almacenar valores como números, cadenas, booleanos, entre otros, y poder manipularlos a lo largo del programa.
"""

# =====================================================
# 1. Sintaxis básica
# =====================================================

# Asignación de una cadena
ciudad = 'Bogotá'
print('Vivo en', ciudad)

# Asignación de enteros y operación aritmética
numero1 = 2
numero2 = 4
suma = numero1 + numero2
print('La suma es:', suma)

# Asignación de un booleano
es_mayor_edad = True
print('¿Es mayor de edad?', es_mayor_edad)

# Asignación de texto y reasignación posterior
animal = 'Perro'
print('Animal:', animal)
animal = 'Gato'
print('Animal:', animal)

# Uso de f-strings para interpolación
nombre = 'Elkin'
edad = 28
print(f'{nombre} tiene {edad} años')

# =====================================================
# 2. Casos de uso comunes
# =====================================================

# Variables para operaciones comerciales
producto = 'pc'
precio = 1000
cantidad = 5
total = precio * cantidad
print(f'El total del producto {producto} es {total}')

# =====================================================
# 3. Buenas prácticas
# =====================================================

# - Usar nombres descriptivos para las variables.
# - Escribir los nombres de variables en snake_case.
# - Declarar e inicializar variables antes de usarlas.
# - Evitar utilizar nombres que coincidan con funciones o tipos integrados de Python (por ejemplo, list, str, sum).

# =====================================================
# 4. Errores comunes
# =====================================================

# - Usar una variable que no ha sido definida (NameError).
# - Confundir nombres de variables por mayúsculas/minúsculas (Python distingue entre `edad` y `Edad`).
# - Reasignar una variable sin darse cuenta, lo cual puede cambiar su valor en tiempo de ejecución.

# =====================================================
# 5. Recursos adicionales
# =====================================================

# Documentación oficial de Python:
# https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

# Convenciones de nombres (PEP 8):
# https://peps.python.org/pep-0008/#naming-conventions