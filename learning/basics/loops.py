# Tema: loops

""" 
Un loop es una estructura que permite repetir un bloque de código varias veces de forma automática 
En Python hay dos tipos principales de loops:
- for: Se usa para recorrer secuencias (listas, tuplas, cadenas, rangos, etc)
- while: Se usa para repetir un bloque de código mientras una condición sea verdadera
"""
# Tema: Bucles

"""
Descripción:
Permiten ejecutar un bloque de código varias veces. Python ofrece bucles while y for, junto con instrucciones como break, continue y pass para controlar el flujo.
"""

# Sintaxis básica

conteo = 0
while conteo < 5:
    print(conteo)
    conteo += 1

conteo = 0
while conteo < 5:
    print(conteo)
    conteo += 1
else:
    print(f"Resultado del else {conteo}")

conteo = 0
while conteo < 5:
    print(conteo)
    conteo += 1
    if conteo == 3:
        break

conteo = 0
while conteo < 5:
    if conteo == 3:
        conteo += 1
        continue
    print(conteo)
    conteo += 1

# Bucle for con diferentes estructuras

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

cadena = "Python"
for caracter in cadena:
    print(caracter)

tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    print(numero)

persona = {
    "nombre": "Elkin",
    "apellido": "Jaramillo",
    "edad": 27,
    "pais": "Colombia",
    "habilidades": ["SQL", "Python"],
    "direccion": "soacha",
    "codigo_postal": 250052
}
for clave, valor in persona.items():
    print(clave, valor)

empresas = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for empresa in empresas:
    print(empresa)

# break y continue en for

numeros = (1, 2, 3, 4, 5)
for num in numeros:
    if num == 3:
        break
    print(num)

for num in numeros:
    if num == 3:
        continue
    print(num)

# range

print(list(range(11)))
print(set(range(11)))
print(list(range(1, 11, 2)))
print(set(range(1, 11, 2)))

for number in range(11):
    print(number)

for clave in persona:
    if clave == "habilidades":
        for habilidad in persona["habilidades"]:
            print(habilidad)

for number in range(11):
    print(number)
else:
    print("fin del bucle")

# pass

for num in range(11):
    pass
