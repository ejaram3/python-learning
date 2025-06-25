# Tema: Diccionarios

"""
Descripción:
Estructura de datos que almacena pares clave:valor. Es mutable y permite almacenar múltiples tipos de datos. A partir de Python 3.7 mantiene el orden de inserción.
"""

# Sintaxis básica

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car["brand"])

car = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2024}
print(car)

print(len(car))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "black"],
}
print(car)

persona = dict(id=1, name="chachito", age=18)
print(type(persona))

# Acceso a elementos

print(car["brand"])
print(car["colors"])
print(car.get("model"))
print(car.get("engine"))
print(car.get("engine", "not defined"))

# Llaves y valores

print(car.keys())
car["engine"] = {"type": "gasoline"}
print(car.keys())

print(car.values())
car["features"] = "automatic"
print(car.values())

print(car.items())
car["previous_owners"] = 1
print(car)

if "engine" in car:
    print("Yes, exist engine in dict")

# Modificación

print(car["year"])
car["year"] = 2000
print(car["year"])

car.update({"engine": {"type": "Gasoline", "displacement": "1.8L", "horsepower": 140}})
print(car["engine"])

car["mileage"] = 23000
print(car["mileage"])

car.update({"license_plate": "ABC123"})
print(car["license_plate"])

# Eliminación

car.pop("engine")
print(car)

car.update({"engine": {"type": "Gasoline", "displacement": "1.8L", "horsepower": 140}})
print(car)
car.popitem()
print(car)

del car["brand"]
print(car)

del car

car = {"brand": "Toyota", "model": "Corolla", "year": 2022, "color": "gray"}
car.clear()
print(car)

# Ciclos

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "color": "gray",
    "engine": {"type": "Gasoline", "displacement": "1.8L", "horsepower": 140},
    "features": {
        "transmission": "Automatic",
        "air_conditioning": True,
        "touch_screen": True,
        "parking_sensors": False,
    },
    "previous_owners": 1,
    "mileage": 23000,
    "license_plate": "ABC123",
    "service_history": [
        {"date": "2023-03-10", "service": "Oil change"},
        {"date": "2024-01-15", "service": "Tire rotation"},
    ],
}

for x in car:
    print(x)

for x in car:
    print(car[x])

for value in car.values():
    print(value)

for key in car.keys():
    print(key)

for key, value in car.items():
    print(key, ":", value)

# Copias

car1 = car.copy()
car2 = dict(car)
car3 = {**car}

# Anidados

people = {
    "person_1": {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "address": {"city": "Bogotá", "country": "Colombia"},
    },
    "person_2": {
        "name": "Bob",
        "age": 25,
        "email": "bob@example.com",
        "address": {"city": "Medellín", "country": "Colombia"},
    },
}
print(people)

people["person_3"] = {
    "name": "chanchito",
    "age": 4,
    "email": "chanchito@mail.com",
    "address": {"city": "new york", "country": "EEUU"},
}
print(people)

print(people["person_1"]["address"]["city"])

for x, obj in people.items():
    print(x)
    for y in obj:
        print(y, ":", obj[y])

agenda = {
    "jose": {
        "telefono": 2524252,
        "gustos": ["bailar", "cantar", "pintar"],
        "ciudad": "colombia",
    },
    "pedro": {"telefono": 636252, "gustos": ["jugar", "leer"], "ciudad": "peru"},
    "carlos": {"telefono": 73352, "gustos": ["leer", "viajar"], "ciudad": "chile"},
}

for persona, datos in agenda.items():
    if "colombia" in datos["ciudad"]:
        print(f"{persona} es de colombia")

for persona, datos in agenda.items():
    for clave in datos:
        if "gustos" in clave:
            print(persona, datos[clave])

for persona, datos in agenda.items():
    print(f"Datos de {persona}:")
    for clave in datos:
        print(f"    {clave} {datos[clave]}")

"""
clear()         → Elimina todos los elementos
copy()          → Devuelve una copia
fromkeys()      → Crea un nuevo diccionario con claves y un valor
get()           → Devuelve el valor de una clave
items()         → Devuelve lista de pares clave:valor
keys()          → Devuelve lista de claves
pop()           → Elimina un elemento por clave
popitem()       → Elimina el último par insertado
setdefault()    → Devuelve valor si existe, si no, inserta con valor dado
update()        → Actualiza o añade elementos
values()        → Devuelve todos los valores
"""
