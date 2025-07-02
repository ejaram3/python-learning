# =====================================================
# Ejercicios: Nivel 1
# =====================================================

# 1. Edad para aprender a conducir
# - Pide al usuario que ingrese su edad usando input("Ingresa tu edad: ").
# - Si el usuario tiene 18 años o más, muestra un mensaje que diga que tiene la edad suficiente para aprender a conducir.
# - Si es menor de 18 años, muestra un mensaje que diga cuántos años faltan para que pueda aprender a conducir.

try:
import math
 edad = int(input("Ingresa tu edad: "))
  print(f"Tu edad es {edad}")
   if edad > 17:
        print("Tiene edad suficiente para aprender a conducir")
    else:
        print(f"Te falta {18 - edad} años para aprender a conducir")
except ValueError:
    print("Debes ingresar un valor entero")

# 2. Comparar edades
# - Define tu edad en una variable llamada mi_edad.
# - Pide al usuario que ingrese su edad usando input("Ingresa tu edad: ").
# - Compara ambas edades:
#   - Si el usuario es mayor, muestra cuántos años mayor es.
#   - Si tú eres mayor, muestra cuántos años mayor eres.
#   - Si tienen la misma edad, muestra un mensaje que diga que tienen la misma edad.
# - Usa "año" si la diferencia es 1, y "años" si es mayor a 1.
mi_edad = 27

try:
    edad = int(input("Ingresa tu edad: "))
    diferencia = abs(edad - mi_edad)
    if edad > mi_edad:
        mensaje = "El usuario es mayor"
    elif mi_edad > edad:
        mensaje = "Yo soy mayor"
    else:
        print("Tienen la misma edad")
        exit()

    anio = "año" if diferencia == 1 else "años"
    print(f"{mensaje} {diferencia} {anio}")

except ValueError:
    print("Debes ingresar un valor entero")


# 3. Comparar dos números
# - Pide al usuario que ingrese dos números.
# - Muestra un mensaje indicando si el primer número es mayor, menor o igual al segundo número.
try:
    numero_1 = float(input("Ingresa el primer número: "))
    numero_2 = float(input("Ingresa el segundo número: "))
    if numero_1 > numero_2:
        mensaje = "El primer número es mayor"
    elif numero_1 < numero_2:
        mensaje = "El primero numero es menor"
    else:
        mensaje = "Son iguales ambos números"
    print(mensaje)
except ValueError:
    print("Debes ingresar un tipo númerico")
# =====================================================
# Ejercicios: Nivel 2
# =====================================================

# 4. Asignar calificación
# - Pide al usuario que ingrese una nota entre 0 y 100.
# - Según el valor, muestra la calificación correspondiente:
#   - 80-100: A
#   - 70-79: B
#   - 60-69: C
#   - 50-59: D
#   - 0-49: F
try:
    input_nota = float(input("Ingresa la nota: "))
    if input_nota in range(1, 101):
        if input_nota in range(1, 50):
            nota = "F"
        elif input_nota in range(50, 60):
            nota = "D"
        elif input_nota in range(60, 70):
            nota = "C"
        elif input_nota in range(70, 80):
            nota = "B"
        else:
            nota = "A"
        print(f"Su calificación es {nota}")

    else:
        print("Nota fuera de rango \"0-100\"")

except ValueError:
    print("Debes ingresar un número")
# 5. Determinar la estación
# - Pide al usuario que ingrese un mes.
# - Muestra la estación del año correspondiente:
#   - Otoño: septiembre, octubre, noviembre
#   - Invierno: diciembre, enero, febrero
#   - Primavera: marzo, abril, mayo
#   - Verano: junio, julio, agosto
mes = input("Ingresa un mes: ").lower()

otonio = ["septiembre", "octubre", "noviembre"]
invierno = ["diciembre", "enero", "febrero"]
primavera = ["marzo", "abril", "mayo"]
verano = ["junio", "julio", "agosto"]

if mes in otonio:
    estacion = "Otoño"
elif mes in invierno:
    estacion = "Invierno"
elif mes in primavera:
    estacion = "Primavera"
elif mes in verano:
    estacion = "Verano"
else:
    print("Valor invalido!")

print(f"La estacion del año es {estacion}!")

# 6. Verificar fruta en lista
# - Tienes una lista con estas frutas: ['banana', 'naranja', 'mango', 'limón'].
# - Pide al usuario que ingrese el nombre de una fruta.
# - Si la fruta no existe en la lista, añádela y muestra la lista actualizada.
# - Si la fruta ya existe, muestra un mensaje que diga que la fruta ya está en la lista.
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta = input("Ingresa una fruta ").lower()
if fruta in frutas:
    print(f"La fruta {fruta} ya existe")
else:
    frutas.append(fruta)
    print(frutas)

# =====================================================
# Ejercicios: Nivel 3
# =====================================================

# 7. Trabajar con un diccionario de persona
# - Tienes un diccionario con información de una persona, incluyendo sus habilidades.
# - Verifica si el diccionario tiene la clave habilidades. Si la tiene:
#   - Muestra la habilidad que está en el medio de la lista de habilidades.
#   - Verifica si la persona tiene la habilidad Python y muestra el resultado.

#   - Según las habilidades de la persona, muestra un mensaje:
#     - Si tiene solo JavaScript y React: “Es un desarrollador front end.”
#     - Si tiene Node, Python y MongoDB: “Es un desarrollador backend.”

#     - Si tiene React, Node y MongoDB: “Es un desarrollador fullstack.”

#     - Si no cumple con lo anterior: “Título desconocido.”
# - Si la persona está casada y vive en Finlandia, muestra un mensaje con su nombre completo y que está casado y vive en Finlandia.

persona = {
    "nombre": "Ana Gómez",
    "edad": 28,
    "email": "ana.gomez@ejemplo.com",
    "pais": "Colombia",
    "habilidades": [
        "Python",
        "SQL",
        "Node",
        "JavaScript",
        "React",
        "MongoDB",
        "Node"
    ],
    "experiencia": {
        "años": 4,
        "último_puesto": "Especialista en Datos"
    }
}
if "habilidades" in persona:
    habilidades = list(dict.fromkeys(persona["habilidades"]))
    centro_idx = len(habilidades) // 2
    habilidad_centro = habilidades[centro_idx]
    print(f"Habilidad del centro: {habilidad_centro}")

    if "Python" in habilidades and "MongoDB" in habilidades and "Node" in habilidades:
        print("Es un desarrollador fullstack.")
    elif "Python" in habilidades and "MongoDB" in habilidades:
        print("Es un desarrollador backend.")
    elif "JavaScript" in habilidades and "React" in habilidades:
        print("Es un desarrollador front end.")
    elif "Python" in habilidades:
        print("Es un desarrollador Python.")
    else:
        print("Título desconocido.")
else:
    print("Título desconocido.")
