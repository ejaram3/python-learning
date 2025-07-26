# 1. Filtra solo negativo y cero en la lista usando la comprensión de la lista
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [number for number in numbers if number < 1]

# 2. Aplanar la siguiente lista de listas de listas a una lista unidimensional

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_list = [num for lvl1 in list_of_lists for lvl2 in lvl1 for num in lvl2]

# print(flat_list)

# 3. Usando la comprensión de listas, cree la siguiente lista de tuplas:

tuples = [(n, 1, n, n ** 2, n ** 3, n ** 4, n ** 5)
          for n in range(11)]

# 4. Aplanar la siguiente lista a una nueva lista

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

flat_list = [[item[0].upper(), item[0][:3].upper(), item[1].upper()]
             for lvl1 in countries for item in lvl1]

# 5. Cambie la siguiente lista a una lista de diccionarios
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_dict = [{'country': item[0], 'city': item[1]}
             for lvl1 in countries for item in lvl1]

# 6. Cambie la siguiente lista de listas a una lista de cadenas concatenadas
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]

flat_list = [item for lvl1 in names for lvl2 in lvl1 for item in lvl2]

# 7. Escriba una función lambda que pueda resolver una pendiente o intersección y de funciones lineales.
earring = lambda modo, p1, p2=None, m=None: \
    ( (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2 and p2[0] != p1[0] else float('inf') ) if modo == "pendiente" \
    else ( p1[1] - m * p1[0] if m is not None else None )

# print(earring("pendiente", (1, 2), (3, 6)) )
# print(earring("interseccion", (3, 6), m=2))