# =====================================================
# Ejercicios: Nivel 1
# =====================================================

# Declarar una función agregar_dos_números. Toma dos parámetros y devuelve una suma.
def agregar_dos_numeros(num1, num2):
    return num1 + num2

# El área de un círculo se calcula de la siguiente manera: área = π xrxr. Escribe una función que calcule área_del_círculo.


def area_circulo(radio):
    PI = 3.14
    return PI * (radio**2)

# Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y sume todos los argumentos.
# Compruebe si todos los elementos de la lista son tipos de números. En caso contrario, proporcione una retroalimentación razonable.


def add_all_nums(*args):
    resultado = 0
    for i in args:
        if isinstance(i, (int, float)):
            resultado += i
        else:
            return "Error, debes ingresar valores de tipo número"
    return resultado

# La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32.
# Escribe una función que convierta °C en °F, convertir_celsius_a-fahrenheit.


def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Escriba una función llamada check-season, toma un parámetro mensual y devuelve la temporada: otoño, invierno, primavera o verano.
estaciones = {
    "Primavera": ["Marzo", "Abril", "Mayo"],
    "Verano": ["Junio", "Julio", "Agosto"],
    "Otoño": ["Septiembre", "Octubre", "Noviembre"],
    "Invierno": ["Diciembre", "Enero", "Febrero"]
}


def revisa_estacion(mes, estaciones_dict=estaciones):
    mes = mes.title()
    for estacion, meses in estaciones_dict.items():
        if mes in meses:
            return estacion
    return "Mes no válido"

# Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal


def pendiente_ecuacion(x: tuple, y: tuple):
    x1, x2 = x
    y1, y2 = y

    if x2 == x1:
        raise ValueError("La pendiente es indefinida (división por cero)")

    return (y2 - y1) / (x2 - x1)

# La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0.
# Escriba una función que calcule el conjunto de soluciones de una ecuación cuadrática, resolver_ecuación_cuadrática.


def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + (discriminante)**0.5) / (2*a)
        x2 = (-b - (discriminante)**0.5) / (2*a)
        return x1, x2

    elif discriminante == 0:
        x = -b / (2*a)
        return x,

    else:
        parte_real = -b / (2*a)
        parte_imaginaria = ((-discriminante)**0.5) / (2*a)
        x1 = complex(parte_real, parte_imaginaria)
        x2 = complex(parte_real, -parte_imaginaria)
        return x1, x2

# Declarar una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.


def imprime_lista(lista: list) -> str:
    for item in lista:
        print(item)


# Declarar una función llamada reverse_list. Toma una matriz como parámetro y devuelve lo contrario de la matriz (use bucles).
# print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
lista = [1, 2, 3, 4, "Hola", True]


def reversar_lista(secuencia):
    for i in range(len(secuencia) - 1, -1, -1):
        yield secuencia[i]


lista_reversa = list(reversar_lista(lista))

# Declarar una función llamada capitalize_list_items. Toma una lista como parámetro y devuelve una lista en mayúsculas de elementos

lista = ["hola", "mundo", "desde", "python"]


def capitalizar_elementos_lista(secuencia: list):
    acumulador = []
    for i in secuencia:
        if isinstance(i, str):
            acumulador.append(i.upper())
        else:
            raise ValueError("Hay valores diferentes a string en la lista")
    return acumulador


# Declarar una función llamada add_item. Toma una lista y parámetros de un elemento. Devuelve una lista con el elemento agregado al final.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
lista = ["hola", "mundo", "desde", "python"]


def suma_item(secuencia: list, elemento):
    secuencia.append(elemento)
    return secuencia

# Declarar una función llamada remove_item. Toma una lista y parámetros de un elemento. Devuelve una lista con el elemento eliminado de ella.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]


def eliminar_item(secuencia: list, elemento):
    secuencia.remove(elemento)
    return secuencia


# Declarar una función llamada suma_de_números. Toma un parámetro numérico y suma todos los números en ese rango.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

def suma_numeros(rango):
    resultado = 0
    for i in range(rango+1):
        resultado += i
    return resultado

# Declarar una función llamada suma_de_probabilidades. Toma un parámetro numérico y suma todos los números impares en ese rango.


def suma_impares(rango):
    resultado = 0
    for i in range(rango + 1):
        if i % 2 != 0:
            resultado += i
    return resultado

# Declarar una función llamada suma_de_par. Toma un parámetro numérico y suma todos los números pares en ese rango.


def suma_pares(rango):
    resultado = 0
    for i in range(rango + 1):
        if i % 2 == 0:
            resultado += i
    return resultado


# =====================================================
# Ejercicios: Nivel 2
# =====================================================

# Declarar una función llamada evens_and_odds. Toma un número entero positivo como parámetro y cuenta el número de pares y probabilidades en el número.
# print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

def evens_and_odds(numero: int):
    pares = 0
    impares = 0

    for i in range(numero + 1):  
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"The number of odds are {impares}.")
    print(f"The number of evens are {pares}.")


evens_and_odds(100)

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
