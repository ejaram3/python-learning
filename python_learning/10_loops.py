# Tema: loops

""" 
Un loop es una estructura que permite repetir un bloque de código varias veces de forma automática 
En Python hay dos tipos principales de loops:
- for: Se usa para recorrer secuencias (listas, tuplas, cadenas, rangos, etc)
- while: Se usa para repetir un bloque de código mientras una condición sea verdadera
"""

# # while
# i = 1
# while i < 6:
#     print(i)
#     i += 1

# # Declaración de break, para detener el bloque de código
# i = 1
# while i < 11:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# # Declaración de continue
# i = 1
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# # Sentencia else
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i ya no es menor que 6")

# # Bucles For
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# # Bucle a traves de cadenas
# for x in "banana":
#     print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# # Declaracion de contienue
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# # funcion range()
# for x in range(6):
#     print(x)

# # definico de rango
# for x in range(2, 6):
#     print(x)

# # Incrementa la secuencia con 3
# for x in range(2, 30, 3):
#     print(x)

# Else en bucle for