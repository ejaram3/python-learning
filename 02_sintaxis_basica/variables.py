# Tema: Variables

"""
Descripción:
Las variables en Python son espacios en memoria usados para guardar datos.
No requieren declaración explícita de tipo debido a que Python es un lenguaje de tipado dinámico.
Se utilizan para almacenar valores como números, cadenas, booleanos, entre otros, y poder manipularlos a lo largo del programa.
"""

# Sintaxis básica

ciudad = 'Bogotá'
print('Vivo en', ciudad)

numero_1 = 2
numero_2 = 4
suma = numero_1 + numero_2
print('La suma es:', suma)

es_mayor_edad = True
print('¿Es mayor de edad?', es_mayor_edad)

animal = 'Perro'
print('Animal:', animal)
animal = 'Gato'
print('Animal:', animal)

nombre = 'Elkin'
edad = 28
print(f'{nombre} tiene {edad} años')

# Casos de uso comunes

producto = 'pc'
precio = 1000
cantidad = 5
total = precio * cantidad
print(f'El total del producto {producto} es {total}')