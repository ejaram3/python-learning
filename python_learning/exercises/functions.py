# =====================================================
# Ejercicios: Nivel 1
# =====================================================

# Declarar una función agregar_dos_números. Toma dos parámetros y devuelve una suma.
def suma_dos_numeros(a, b):
    return a + b


# print(suma_dos_numeros(4, 6))

# El área de un círculo se calcula de la siguiente manera: área = π xrxr. Escribe una función que calcule área_del_círculo.


def area_circulo(radio):
    PI = 3.14
    return PI * radio ** 2


# print(area_circulo(2))

# Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y sume todos los argumentos. Compruebe si todos los elementos de la lista son tipos de números. En caso contrario, proporcione una retroalimentación razonable.


def agrega_todos_numeros(*args):
    acumulador = 0
    for i in args:
        if not (isinstance(i, (int, float))):
            return "Error, todos los elementos deben ser de tipo número"
        acumulador += i
    return acumulador


print(agrega_todos_numeros(1, 3, 6, 10))


# La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C en °F, convertir_celsius_a-fahrenheit.

# Escriba una función llamada check-season, toma un parámetro mensual y devuelve la temporada: otoño, invierno, primavera o verano.

# Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal

# La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0.
# Escriba una función que calcule el conjunto de soluciones de una ecuación cuadrática, resolver_ecuación_cuadrática.

# Declarar una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.

# Declarar una función llamada reverse_list. Toma una matriz como parámetro y devuelve lo contrario de la matriz (use bucles).
# print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

# Declarar una función llamada capitalize_list_items. Toma una lista como parámetro y devuelve una lista en mayúsculas de elementos

# Declarar una función llamada add_item. Toma una lista y parámetros de un elemento. Devuelve una lista con el elemento agregado al final.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

# Declarar una función llamada remove_item. Toma una lista y parámetros de un elemento. Devuelve una lista con el elemento eliminado de ella.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]

# Declarar una función llamada suma_de_números. Toma un parámetro numérico y suma todos los números en ese rango.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

# Declarar una función llamada suma_de_probabilidades. Toma un parámetro numérico y suma todos los números impares en ese rango.

# Declarar una función llamada suma_de_par. Toma un parámetro numérico y suma todos los números pares en ese rango.

# =====================================================
# Ejercicios: Nivel 2
# =====================================================

# Declarar una función llamada evens_and_odds. Toma un número entero positivo como parámetro y cuenta el número de pares y probabilidades en el número.
# print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

# Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número

# Llama a tu función está_vacío, toma un parámetro y comprueba si está vacío o no

# Escriba diferentes funciones que tomen listas.
# Deben calcular_media, calcular_mediana, calcular_modo, calcular_rango, calcular_varianza, calcular_std (desviación estándar).

# =====================================================
# Ejercicios: Nivel 3
# =====================================================

# Escriba una función llamada is_prime, que verifique si un número es primo.

# Escriba una función que verifique si todos los elementos son únicos en la lista.

# Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos.

# Escriba una función que verifique si la variable proporcionada es una variable de Python válida

# Vaya a la carpeta de datos y acceda al archivo countries-data.py.

# Crea una función llamada los idiomas_más_hablados del mundo.
# Debería devolver 10 o 20 de los idiomas más hablados del mundo en orden descendente

# Crea una función llamada los países_más_poblados.
# Debería devolver 10 o 20 países más poblados en orden descendente.
