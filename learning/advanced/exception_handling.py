# Tema: Manejo de excepciones try-except
""" 
El manejo de excepciones con try...except es una forma de controlar errores que ocurren durante la ejecución de un programa. El código que podría generar un error se coloca dentro de un bloque try, y si ocurre una excepción, la ejecución del bloque try se detiene y el programa salta al bloque except correspondiente, evitando que el programa se detenga bruscamente
"""
# try:
#     print(10 + "2")
# except:
#     print("Algo salió mal")

# from datetime import datetime
# try:
#     name = input("Ingresa tu nombre: ")
#     year_born = input("Ingresa el año que naciste: ")
#     age = datetime.now().year - year_born
#     print(f"Tu nombre es {name} y tu edad es {age}.")

# except:
#     print("Algo salió mal")


# from datetime import datetime
# try:
#     name = input("Ingresa tu nombre: ")
#     year_born = input("Ingresa el año que naciste: ")
#     age = datetime.now().year - year_born
#     print(f"Tu nombre es {name} y tu edad es {age}.")

# except TypeError:
#     print("Se ha producido un error de tipo")
# except ValueError:
#     print("Se ha producido un error de valor")
# except ZeroDivisionError:
#     print("Se produjo un error de división cero")
# else:
#     print("Normalmente corro con el bloque de prueba")
# finally:
#     print("Yo siempre corro")

# # También se acorta el código anterior de la siguiente manera
# from datetime import datetime
# try:
#     name = input("Ingresa tu nombre: ")
#     year_born = input("Ingresa el año que naciste: ")
#     age = datetime.now().year - year_born
#     print(f"Tu nombre es {name} y tu edad es {age}.")
# except Exception as e:
#     print(e)

# Argumentos de embalaje y desempaquetado en Python
# Se utilizan dos operadores: * para tuplas, ** para diccionarios

# Desembalaje
def sum_of_five_numbers(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
# print(sum_of_five_numbers(lst))  # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
print(sum_of_five_numbers(*lst))

# También se puedes usar desempaquetado en la función incorporada de rango
numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

# Una lista o una tupla también se puede desempaquetar así
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)

# Desempaquetar diccionarios


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Elkin', 'country': 'Colombia', 'city': 'Bogota', 'age': 28}
print(unpacking_person_info(**dct))

# Embalaje


def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# Diccionario de embalaje


def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Elkin",
      country="Colombia", Colombia="Bogota", age=28))

# Difusión en Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# Enumerar
for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = nordic_countries
for index, i in enumerate(countries):
    print("hi")
    if i == "Finland":
        print(f"The country {i} has been found at index {index}")

# CP
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({"fruit": f, "veg": v})

print(fruits_and_veges)
