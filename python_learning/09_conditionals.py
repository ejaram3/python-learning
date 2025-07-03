# Tema: if elif else

"""
Descripción:
Permiten ejecutar diferentes bloques de código según condiciones. 
- if: evalúa una condición; si es verdadera, ejecuta su bloque.
- elif: evalúa otra condición si las anteriores fueron falsas.
- else: se ejecuta si ninguna condición anterior fue verdadera.

Python soporta condiciones lógicas y operadores de comparación:
== igual a
!= no igual a
<  menor que
>  mayor que
<= menor o igual a
>= mayor o igual a
"""

# Sintaxis básica

a = 33
b = 200
if b > a:
    print("b es mayor que a")

a = 33
b = 33
if b > a:
    print("b es mayor que a")
elif b == a:
    print("b es igual que a")

a = 200
b = 33
if b > a:
    print("b es mayor que a")
elif b == a:
    print("b es igual que a")
else:
    print("a es mayor que b")

# Condición en una línea

if a > b: print("a es mayor que b")

# Operador ternario

a = 2
b = 200
print("A") if a > b else print("B")

# Operadores lógicos

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Ambas condiciones son verdaderas")

c = 100
if a > b or c > a:
    print("Al menos una de las condiciones es verdadera")

if not a > b:
    print("a no es mayor que b")

# if anidados

x = 41
if x > 10:
    print("Por encima de diez")
    if x > 20:
        print("y ¡También por encima de 20!")
    else:
        print("Pero no por encima de 20")

# Uso de pass

if b > a:
    pass
print("Funciona pass")
