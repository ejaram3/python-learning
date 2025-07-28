# Tema: Funciones de orden superior

"""
Descripción:
Una función de orden superior es aquella que cumple con al menos los siguientes parámetros:
- Recibe una función como argumento
- Devuelve una función como resultado
"""

# Función como parámetro

def sumar_lista(numeros):
    return sum(numeros)

def funcion_orden_superior(funcion, lista):
    return funcion(lista)

resultado = funcion_orden_superior(sumar_lista, [1, 2, 3, 4, 5])
print(resultado)

# Función como valor de retorno

def cuadrado(numero):
    return numero ** 2

def cubo(numero):
    return numero ** 3

def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return -numero

def seleccionar_funcion(tipo):
    if tipo == "cuadrado":
        return cuadrado
    elif tipo == "cubo":
        return cubo
    elif tipo == "absoluto":
        return valor_absoluto

funcion_cuadrado = seleccionar_funcion("cuadrado")
print(funcion_cuadrado(3))

funcion_cubo = seleccionar_funcion("cubo")
print(funcion_cubo(3))

funcion_absoluto = seleccionar_funcion("absoluto")
print(funcion_absoluto(-3))

# Cierres en Python (closures)

def suma_diez():
    constante = 10

    def suma(valor):
        return valor + constante
    return suma

resultado_closure = suma_diez()
print(resultado_closure(5))
print(resultado_closure(10))

# Decoradores en Python

# Decorador manual

def decorador_mayusculas(funcion):
    def envoltura():
        resultado = funcion()
        return resultado.upper()
    return envoltura

def saludar():
    return "Bienvenido a Python"

funcion_decorada = decorador_mayusculas(saludar)
print(funcion_decorada())

# Decorador con sintaxis @

@decorador_mayusculas
def saludar_python():
    return "Bienvenido a python con elkin"

print(saludar_python())

# Múltiples decoradores

def decorador_convertir_mayusculas(funcion):
    def envoltura():
        return funcion().upper()
    return envoltura

def decorador_separar_string(funcion):
    def envoltura():
        return funcion().split()
    return envoltura

@decorador_separar_string
@decorador_convertir_mayusculas
def mensaje_bienvenida():
    return "Bienvenido a python"

print(mensaje_bienvenida())

# Decoradores con parámetros

def decorador_con_parametros(funcion):
    def envoltura(nombre, apellido, pais):
        funcion(nombre, apellido, pais)
        print("Yo vivo en {}".format(pais))
    return envoltura

@decorador_con_parametros
def nombre_completo(nombre, apellido, pais):
    print("Yo soy {} {}. Me encanta enseñar.".format(nombre, apellido))

nombre_completo("Elkin", "Jaramillo", "Colombia")

# Funciones integradas de orden superior: map, filter, reduce

# map()

numeros = [1, 2, 3, 4, 5, 6, 7]

cuadrados = map(lambda numero: numero ** 2, numeros)
print(list(cuadrados))

numeros_texto = ['1', '2', '3', '4', '5']
numeros_enteros = map(int, numeros_texto)
print(list(numeros_enteros))

nombres = ["Elkin", "Pedro", "Carla"]
nombres_mayusculas = map(lambda nombre: nombre.upper(), nombres)
print(list(nombres_mayusculas))

# filter()

numeros = [1, 2, 3, 4, 5, 6, 7]
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares))

nombres = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
nombres_largos = filter(lambda nombre: len(nombre) > 7, nombres)
print(list(nombres_largos))

# reduce()

from functools import reduce

numeros_texto = ['1', '2', '3', '4', '5']

suma_dos_numeros = lambda x, y: int(x) + int(y)

resultado_total = reduce(suma_dos_numeros, numeros_texto)
print(resultado_total)