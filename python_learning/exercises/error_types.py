# Ejercicios sin manejo de errores
# Suma de tipos incompatibles
a = "10"
b = 5
# resultado = a + b
resultado = int(a) + b

# Acceso a índice fuera de rango
lista = [1, 2, 3]
# valor = lista[10]
valor = lista[2]

# Conversión inválida a entero
# valor = int("abc123")
valor = str("abc123")

# División por cero
# x = 100 / 0
x = 100 / 1

# Acceso a clave inexistente
d = {"nombre": "Elkin"}
# valor = d["edad"]
valor = d["nombre"]

# Uso de variable no definida
# print(variable_inexistente)
variable_inexistente = 'hola'
print(variable_inexistente)

# Ejercicios con manejo de errores
# Maneja la división por cero
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        return f"Error, no puedes dividir por Cero: {err}"

print(dividir(10, 0))

# Lectura de archivo inexistente
def leer_archivo(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError as err:
        return f"No se encuentro el archivo: {err}"

print(leer_archivo("no_existe.txt"))

# Conversión de string a entero con validación
def convertir(valor):
    try: 
        return int(valor)
    except ValueError as err:
        return f"Debes ingresar un entero: {err}"

print(convertir("no_es_numero"))


# Manejo general de excepción desconocida
def operacion():
    try:
        x = "10" + 5
    except TypeError as err:
        return err

print(operacion())


# Itera una lista y maneja errores por tipo
valores = [10, "20", None, "abc", 5]

acc = []
for v in valores:
    try:
        acc.append(int(v))
        print(f"Valores convertido: {acc}")
    except TypeError:
        print(f"TypeError: No se puede convertir el tipo {type(v)}")
    except ValueError:
        print(f"ValueError: El valor '{v}' no es convertible a entero")
