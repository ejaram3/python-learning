# =====================================================
# Ejercicios: Nivel 1
# =====================================================

# Escriba una función que genere un random_user_id de seis dígitos/caracteres.
# print(random_user_id());
# '1ee33d'
#
import re
import random
import string
import string
import random


def usuario_aleatorio():
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

# print(usuario_aleatorio())

# Modifica la tarea anterior. Declarar una función llamada user_id_gen_by_user.
# No toma ningún parámetro, pero toma dos entradas usando input().
# Una de las entradas es el número de caracteres y la segunda entrada es el número de ID que se supone que se generan.
# print(user_id_gen_by_user()) # user input: 5 5
# output:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf
#
# print(user_id_gen_by_user()) # 16 5
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr


def generar_ids_usuarios(longitud_id, cantidad):
    caracteres = string.ascii_lowercase + string.digits + string.ascii_uppercase
    for _ in range(cantidad):
        print(''.join(random.choice(caracteres) for _ in range(longitud_id)))

# logitud_id = int(input("Ingresa la longitud: "))
# cantidad = int(input("Ingresa la cantidad de usuarios a generar: "))
# generar_ids_usuarios(logitud_id, cantidad)

# Escribe una función llamada rgb_color_gen. Generará colores rgb (3 valores que van de 0 a 255 cada uno).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form


def rgb_color_gen():
    return f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"


# =====================================================
# Ejercicios: Nivel 2
# =====================================================
# Escriba una función list_of_hexa_colors que devuelva cualquier número de colores hexa en una matriz


def list_of_hexa_colors(cantidad):
    matriz_hexa_colores = []
    caracteres = re.sub(r"[a-f]", "", string.hexdigits)
    for _ in range(cantidad):
        matriz_hexa_colores.append(
            ''.join(random.choice(caracteres) for _ in range(6)))
    return matriz_hexa_colores
# Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.


def list_of_rgb_colors(cantidad):
    matriz_rgb_colors = []
    for _ in range(cantidad):
        matriz_rgb_colors.append(
            f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})")
    return matriz_rgb_colors


# Escribe una función generate_colors que pueda generar cualquier número de colores hexa o rgb.
# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(tipo, cantidad):
    if tipo.lower() == "hex":
        resultado = list_of_hexa_colors(cantidad=cantidad)
    elif tipo.lower() == "rgb":
        resultado = list_of_rgb_colors(cantidad=cantidad)
    else:
        resultado = "Invalido"
    return resultado


# =====================================================
# Ejercicios: Nivel 3
# =====================================================

# Llame a su función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria

def shuffle_list(lista):
    random.shuffle(lista)
    return lista

# Escriba una función que devuelva una matriz de siete números aleatorios en un rango de 0 a 9.
# Todos los números deben ser únicos.


def numeros_aleatorios():
    return "".join(str(d) for d in random.sample(range(10), 7))
