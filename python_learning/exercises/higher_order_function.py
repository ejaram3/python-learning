import json
from countries import countries
from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejercicios: Nivel 1

# Explica la diferencia entre mapear, filtrar y reducir.

# map(): aplica una función a cada elemento de un iterable y devuelve un nuevo iterable con el mismo número de elementos transformados.
# filter(): aplica una función booleana a cada elemento de un iterable y devuelve solo los elementos para los que la función retorna True.
# reduce(): aplica una función acumuladora de dos argumentos a los elementos de un iterable, reduciéndolo a un solo valor.

# Explica la diferencia entre la función de orden superior, el cierre y el decorador
# Función de orden superior: recibe al menos una función como argumento y devuelve una función como resultado
# Función de cierre (closure): es una función interna que recuerda el valor de la variable del ámbito externo en el momento que fue definida incluso si ese ámbito ya no existe
# Decorador: es una función de orden superior que recibe una función como entrada y envuelve con lógica adicional y devuelve una nueva función modificada, manteniendo la interfaz original

# Defina una función de llamada antes de mapear, filtrar o reducir, ver ejemplos.

# Función para verificar si un número es par


def is_evens(number):
    return number % 2 == 0

# Función para elevar al cuadrado


def square(number):
    return number ** 2

# Función para sumar dos o más números


def add(a, b):
    return int(a) + int(b)


# Aplicar map (elevar al cuadrado)
square_of_numbers = map(square, numbers)
print(list(square_of_numbers))

# Aplicar filter (filtrar pares)
numbers_evens = filter(is_evens, numbers)
print(list(numbers_evens))

# Aplicar reduce (sumar todos)
add_numbers = reduce(add, numbers)
print(add_numbers)

# Usa for loop para imprimir cada país en la lista de países.
for country in countries:
    print(country)
# Úselo para imprimir cada nombre en la lista de nombres.
for name in names:
    print(name)
# Úselo para imprimir cada número de la lista de números.
for number in numbers:
    print(number)


# Ejercicios: Nivel 2

# Usa el mapa para crear una nueva lista cambiando cada país a mayúsculas en la lista de países
countries_in_uppercase = map(lambda country: country.upper(), countries)
print(list(countries_in_uppercase))

# Usa el mapa para crear una nueva lista cambiando cada número a su cuadrado en la lista de números
numbers_square = map(lambda number: number ** 2, numbers)
print(list(numbers_square))

# Usa el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
names_in_uppercase = map(lambda name: name.upper(), names)
print(list(names_in_uppercase))

# Utilice el filtro para filtrar los países que contienen "land".
tierra_in_countries = filter(lambda country: 'land' in country, countries)
print(list(tierra_in_countries))

# Utilice el filtro para filtrar países que tengan exactamente seis caracteres.
len_6_countries = filter(lambda country: len(country) == 6, countries)
print(list(len_6_countries))

# Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.


def countries_letter_greater_6(country):
    if len(countries) >= 6:
        return True
    return False


countries_letter_greater_6 = filter(countries_letter_greater_6, countries)
print(list(countries_letter_greater_6))

# Usa el filtro para filtrar los países que comienzan con una "E"
startwith_e = filter(lambda country: str(
    country).upper().startswith("E"), countries)
print(list(startwith_e))

# Encadena dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback))
string_several = reduce(
    lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(string_several)

# Declara una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
lists = [1, "saludo", True, False, 2.3, "Hola", "Python"]


def get_string_lists(lst):
    if isinstance(lst, str):
        return True
    return False


string_lists = filter(get_string_lists, lists)
print(list(string_lists))

# Use reducir para sumar todos los números de la lista de números.
add_numbers = reduce(lambda a, b: int(a) + int(b), numbers)
print(add_numbers)

# Use reducir para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa
reduce_countries = reduce(lambda a, b: a + ', ' + b,
                          countries) + ' son países del norte de Europa'
print(reduce_countries)

# Declare una función llamada categorize_countries que devuelve una lista de países con algún patrón común (puede encontrar la lista de países en este repositorio como countries.js (por ejemplo, 'land', 'ia', 'island', 'stan')).


def categorize_countries(countries):
    patterns = ['land', 'ia', 'island', 'stan']
    return list(filter(lambda country: any(p in country for p in patterns), countries))


print(categorize_countries(countries))

# Cree una función que devuelva un diccionario, donde las claves representan las letras iniciales de los países y los valores son la cantidad de nombres de países que comienzan con esa letra.


def return_dict(lst):
    return reduce(
        lambda acc, item: acc.update(
            {item[0].upper(): acc.get(item[0].upper(), 0) + 1}) or acc,
        lst,
        {}
    )


print(return_dict(countries))

# Declara una función get_first_ten_countries - devuelve una lista de los primeros diez países de la lista countries.js en la carpeta de datos.


def get_first_ten_countries(lst):
    return lst[:10]


print(get_first_ten_countries(countries))

# Declara una función get_last_ten_countries que devuelve los últimos diez países de la lista de países.


def get_last_ten_countries(lst):
    return lst[-10:]


print(get_last_ten_countries(countries))
# Utilice countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) archivar y seguir las tareas siguientes:

with open("/workspaces/python-learning/python_learning/exercises/countries_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Ordenar países por nombre, capital y población
orden_por_nombre = sorted(data, key=lambda x: x["name"])

orden_por_capital = sorted(data, key=lambda x: x["capital"])

orden_por_poblacion = sorted(data, key=lambda x: x["population"], reverse=True)

list(map(lambda x: print(
    f'{x["name"]} - {x["capital"]} - {x["population"]}'), orden_por_nombre[:5]))

# Ordenar los diez idiomas más hablados por número de países
idioma_paises = reduce(
    lambda acc, country: reduce(
        lambda acc2, lang: acc2.update({lang: acc2.get(lang, 0) + 1}) or acc2,
        set(country["languages"]),
        acc
    ),
    data,
    {}
)

top_10_idiomas = sorted(idioma_paises.items(),
                        key=lambda x: x[1], reverse=True)[:10]

list(map(lambda x: print(f"{x[0]}: {x[1]} países"), top_10_idiomas))

# Ordenar los diez países más poblados
top_10_paises_poblados = sorted(
    data, key=lambda x: x["population"], reverse=True)[:10]

list(map(lambda x: print(
    f"{x['name']}: {x['population']} habitantes"), top_10_paises_poblados))
