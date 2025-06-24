# Tema: Diccionarios
diccionario = {
    "marca": "ford",
    "modelo": "Mustang",
    "anio": 1964,
}
print(diccionario)

print(diccionario["modelo"])

# Longitud
print(len(diccionario))

# Articulos de diccionario - tipos de datos
auto = {
    "marca": "ford",
    "electrico": False,
    "anio": 1964,
    "colores": ["rojo", "blanco", "azul"]
}

print(type(auto))

# Constructor dict()
persona = dict(nombre="Elkin", edad=27, pais="Colombia")
print(persona)

# Acceder a elementos del diccionario
marca = auto["marca"]
print(marca)

# Usando el metodo get() revisive 2 parametros elemento y valor por default si no encuentra valor no arroja error
modelo = auto.get("modelo")
# si no se le asigna ningun valor retorna None
print(modelo)
# se le puede definir un valor por default como segundo parametro
modelo = auto.get("modelo", "sin valor")
print(modelo)

# Obtener llaves
llaves = auto.keys()
print(llaves)

auto["cantidad"] = 3

llaves = auto.keys()
print(llaves)

# Obtener valores
valores = auto.values()
print(valores)

auto["pais"] = "EEUU"

valores = auto.values()
print(valores)

# Obtener articulos o elementos
elementos = auto.items()
print(elementos)

auto["precio"] = 214.521435
print(auto)

elementos = auto.items()
print(elementos)

# Comprobar si un valor existe
# Nota: se valida por claves no por valores
if "marca" in auto:
    print("Existe al marca dentro del diccionario auto")

# Modificar articulos de un diccionario
auto["anio"] = 1999
print(auto["anio"])

# Actualizar un diccionario
auto.update({"anio": 2020})
print(auto["anio"])

# Agregar articulos a un diccionario
auto["motor"] = 3200
print(auto)

# Actualizar diccionario
auto.update({"peso": 2.522})
print(auto)
