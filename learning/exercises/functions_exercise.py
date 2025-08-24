# =====================================================
# Ejercicios: Nivel 1
# =====================================================

# Declarar una función agregar_dos_números. Toma dos parámetros y devuelve una suma.
import json
import keyword
import math


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
# The number of evens are 51.parsssss

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


# evens_and_odds(100)

# Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Llama a tu función está_vacío, toma un parámetro y comprueba si está vacío o no


def esta_vacio(valor):
    if not valor:
        return True
    else:
        return False

# Escriba diferentes funciones que tomen listas.
# Deben calcular_media, calcular_mediana, calcular_modo, calcular_rango, calcular_varianza, calcular_std (desviación estándar).


def mediana(lista: list) -> float:
    if not lista:
        raise ValueError("La lista no puede estar vacía")

    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    medio = n // 2

    if n % 2 == 0:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2
    else:
        return lista_ordenada[medio]


def media(lista: list) -> list:
    base = int(len(lista) / 2)

    if len(lista) % 2 == 0:
        media = lista[base - 1: base + 1]
    else:
        media = lista[base]
    return media


def modo(lista: list):
    resultado = []
    for n in lista:
        resultado.append((n, (lista.count(n))))

    return list(set(resultado))


lista = [1, 2, 4, 5, 1, 2, 4, 2, 1]


def rango(lista: list):
    rango = max(lista) - min(lista)
    return rango


def varianza(datos, poblacional=True):
    n = len(datos)
    media = sum(datos) / n
    suma_cuadrados = sum((x - media) ** 2 for x in datos)

    if poblacional:
        return suma_cuadrados / n
    else:
        return suma_cuadrados / (n - 1)


def desviacion_estandar(datos, poblacional=True):
    n = len(datos)
    media = sum(datos) / n
    suma_cuadrados = sum((x - media) ** 2 for x in datos)

    if poblacional:
        varianza = suma_cuadrados / n
    else:
        varianza = suma_cuadrados / (n - 1)

    return math.sqrt(varianza)

# =====================================================
# Ejercicios: Nivel 3
# =====================================================

# Escriba una función llamada is_prime, que verifique si un número es primo.


def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


# Escriba una función que verifique si todos los elementos son únicos en la lista.

def elementos_unicos(lista: list):
    if len(lista) != len(set(lista)):
        return "Lista con registros duplicados"
    return "Registros únicos en la lista"

# Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos.


def mismo_tipo(lista):
    if not lista:
        return True

    tipo_base = type(lista[0])
    for elem in lista[1:]:
        if type(elem) != tipo_base:
            return False
    return True

# Escriba una función que verifique si la variable proporcionada es una variable de Python válida


def valida_en_python(variable):
    return variable.isidentifier() and not keyword.iskeyword(variable)


# Vaya a la carpeta de datos y acceda al archivo countries-data.py.
# Crea una función llamada los idiomas_más_hablados del mundo.
# Debería devolver 10 o 20 de los idiomas más hablados del mundo en orden descendente

with open("./paises_data.json", "r", encoding="utf-8") as file:
    paises = json.load(file)


def idiomas_mas_hablados(paises):
    idiomas = []
    for elementos in paises:
        for idioma in elementos['languages']:
            idiomas.append(idioma)
    conteo = {}
    for idioma in idiomas:
        if idioma in conteo:
            conteo[idioma] += 1
        else:
            conteo[idioma] = 1

    return dict(
        sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:10])


# Crea una función llamada los países_más_poblados.
# Debería devolver 10 o 20 países más poblados en orden descendente.
def paises_poblados(paises):
    poblaciones = []
    for elementos in paises:
        poblaciones.append((elementos['name'], elementos['population']))

    return dict(
        sorted(poblaciones, key=lambda x: x[1], reverse=True)[:10])


print(paises_poblados(paises))
