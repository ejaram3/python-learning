# Tema: Funciones

"""
Descripción:
Una función es un bloque de código reutilizable que realiza una tarea específica.
- Se define con la palabra clave def.
- Puede tener parámetros o no.
- Puede retornar valores.
"""

# Sintaxis básica


def muestra_nombre_completo():
    nombre = "Elkin"
    apellido = "Jaramillo"
    espacio = " "
    nombre_completo = nombre + espacio + apellido
    print(nombre_completo)


muestra_nombre_completo()


def imprime_suma_dos_numeros():
    numero_1 = 10
    numero_2 = 3
    suma = numero_1 + numero_2
    print(suma)


imprime_suma_dos_numeros()

# Retorno de valores


def retorna_nombre():
    nombre = "Elkin"
    apellido = "Jaramillo"
    espacio = " "
    return nombre + espacio + apellido


print(retorna_nombre())


def retorna_suma_dos_numeros():
    numero_1 = 10
    numero_2 = 3
    return numero_1 + numero_2


print(retorna_suma_dos_numeros())

# Parámetros


def saludo_personal(nombre):
    mensaje = f"{nombre}, bienvenido a Python para todos"
    return mensaje


print(saludo_personal("Elkin"))


def suma_mas_diez(numero):
    return numero + 10


print(suma_mas_diez(67))


def calcula_cuadrado(numero):
    return numero ** 2


print(calcula_cuadrado(5))


def calcula_area_circulo(radio):
    pi = 3.14
    return pi * radio ** 2


print(calcula_area_circulo(2))


def suma_hasta_n(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)


suma_hasta_n(10)
suma_hasta_n(100)


def construir_nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"


print(construir_nombre_completo("Elkin", "Jaramillo"))


def suma_dos_valores(valor_1, valor_2):
    return valor_1 + valor_2


print(suma_dos_valores(3, 4))


def obtener_edad(anio_actual, anio_nacimiento):
    return anio_actual - anio_nacimiento


print("Edad:", obtener_edad(2025, 1997))


def calcular_ancho_objeto(masa, gravedad):
    return str(masa * gravedad) + " N"


print("El ancho del objeto en newtons", calcular_ancho_objeto(100, 9.81))

# Argumentos con clave


def mostrar_nombre_completo(nombre, apellido):
    print(f"{nombre} {apellido}")


mostrar_nombre_completo(nombre="Elkin", apellido="Jaramillo")


def devolver_nombre(nombre, apellido):
    return f"{nombre} {apellido}"


print(devolver_nombre("Elkin", "Jaramillo"))


def sumar_dos_numeros(numero_1, numero_2):
    return numero_1 + numero_2


print(sumar_dos_numeros(3, 4))


def verificar_par(n):
    return n % 2 == 0


print(verificar_par(4))


def obtener_pares(n):
    pares = []
    for i in range(n + 1):
        if i % 2 == 0:
            pares.append(i)
    return pares


print(obtener_pares(10))

# Parámetros predeterminados


def mensaje_bienvenida(nombre="Elkin"):
    return f"{nombre} bienvenido a python para todos"


print(mensaje_bienvenida())
print(mensaje_bienvenida("Juan"))


def nombre_completo_por_defecto(nombre="Elkin", apellido="Jaramillo"):
    return f"{nombre} {apellido}"


print(nombre_completo_por_defecto())
print(nombre_completo_por_defecto("Jose", "Perez"))

# Número arbitrario de argumentos


def sumar_argumentos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total


print(sumar_argumentos(2, 3, 5))

# Parámetro normal y arbitrario


def mostrar_equipo(equipo, *integrantes):
    print(equipo)
    for integrante in integrantes:
        print(integrante)


mostrar_equipo("Equipo 1", "Elkin", "Jose", "Pedro", "Juan")

# Funciones como parámetros


def obtener_cuadrado(n):
    return n * n


def aplicar_funcion(funcion, valor):
    return funcion(valor)


print(aplicar_funcion(obtener_cuadrado, 3))
