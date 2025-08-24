# =====================================================
# EJERCICIOS NIVEL 1
# =====================================================

# 1. Itera del 0 al 10 usando el bucle for.
import json
from paises import countries
for i in range(0, 11):
    print(i)

# 2. Itera del 0 al 10 usando el bucle while.
conteo = 0
while conteo < 11:
    print(conteo)
    conteo += 1

# 3. Itera de 10 a 0 usando el bucle for.
for i in range(10, 0, -1):
    print(i)

# 4. Itera de 10 a 0 usando el bucle while.
conteo = 10
while conteo > 0:
    print(conteo)
    conteo -= 1

# 5. Escribe un bucle que realiza siete llamadas a print() para obtener:
# #
# ##
# ###
# ####
# #####
# ######
# #######

for i in range(1, 8):
    print("#" * i)

# 6. Usa bucles anidados para crear el siguiente patrón:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

for fila in range(9):
    for columna in range(9):
        print("#", end=" ")
    print()


# 7. Imprime el siguiente patrón de cuadrados:
# 0 x 0 = 0
# 1 x 1 = 1
# ...
# 10 x 10 = 100

for i in range(1, 11):
    print(f"{i} x {i} = {i*i}")


# 8. Itera sobre ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] y imprime cada elemento.
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for elemento in lista:
    print(elemento)

# 9. Usa un bucle for para imprimir solo los números pares de 0 a 100.
for numero in range(101):
    if numero % 2 == 0:
        print(numero)

# 10. Usa un bucle for para imprimir solo los números impares de 0 a 100.
for numero in range(101):
    if numero % 2 != 0:
        print(numero)

# =====================================================
# EJERCICIOS NIVEL 2
# =====================================================

# 11. Usa un bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.
# Resultado esperado: The sum of all numbers is 5050
suma_num = 0
for n in range(101):
    suma_num += n
print(suma_num)

# 12. Usa un bucle for para iterar de 0 a 100 e imprimir la suma de los pares y la suma de los impares.
# Resultado esperado: The sum of all evens is 2550. And the sum of all odds is 2500.
par = 0
impar = 0
for n in range(101):
    if n % 2 == 0:
        par += n
    else:
        impar += n
print(f"Par: {par}")
print(f"Impar: {impar}")
# =====================================================
# EJERCICIOS NIVEL 3
# =====================================================

# 13. Recorre la lista de países (del archivo países.py) y extrae los que contienen la palabra 'land'.
for country in countries:
    if "land" in country:
        print(country)
# 14. Dada la lista ['plátano', 'naranja', 'mango', 'limón'] invierte el orden usando un bucle.
lista = ['plátano', 'naranja', 'mango', 'limón']
lista_invertida = []

for i in range(len(lista) - 1, -1, - 1):
    lista_invertida.append(lista[i])
print(lista_invertida)


# 15. Con el archivo países_datos.py:
#     a) ¿Cuál es el número total de idiomas en los datos?
#     b) Encuentra los diez idiomas más hablados a partir de los datos.
#     c) Encuentra los 10 países más poblados del mundo.

with open("./paises_data.json", "r", encoding="utf-8") as file:
    paises = json.load(file)

# Total idiomas
idiomas = []
for elementos in paises:
    for idioma in elementos['languages']:
        idiomas.append(idioma)

print(f"Total idiomas:\n{len(set(idiomas))}")

# Contar idiomas manualmente
conteo = {}
for idioma in idiomas:
    if idioma in conteo:
        conteo[idioma] += 1
    else:
        conteo[idioma] = 1

# 10 idiomas más hablados
top_10_idiomas = dict(
    sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:10])
print(f"Idiomas más hablados:\n{top_10_idiomas}")

# 10 países más poblados
poblaciones = []
for elementos in paises:
    poblaciones.append((elementos['name'], elementos['population']))

top_10_poblacion = dict(
    sorted(poblaciones, key=lambda x: x[1], reverse=True)[:10])
print(f"Países más poblados:\n{top_10_poblacion}")
