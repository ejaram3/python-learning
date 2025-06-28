# =====================================================
# SECCIÓN 1: Creación y acceso
# =====================================================

# 1. Crea un diccionario llamado persona con claves: nombre, edad, ciudad.
persona = {"nombre": "elkin", "edad": 27, "ciudad": "Bogotá"}

# 2. Imprime el valor de la clave "nombre" accediendo con [] y con get().
print(persona["nombre"])
print(persona.get("nombre"))

# 3. Verifica si existe la clave "email" en el diccionario persona.
print("email" in persona)

# 4. Crea un diccionario con al menos 5 claves y distintos tipos de valores (int, str, list, dict, bool).
datos = {
    "persona1": {
        "nombre": "elkin",
        "edad": 27,
        "trabaja": True,
        "pasatiempos": ["estudiar", "gym", "musica"],
    },
}

# 5. Crea un diccionario usando el constructor dict() con al menos dos claves.
datos_persona = dict(
    nombre="elkin",
    edad=27,
    trabaja=True,
    lenguajes_preferidos=["Python", "SQL", "Java"],
)

# =====================================================
# SECCIÓN 2: Modificación y actualización
# =====================================================

# 6. Cambia el valor de la clave "ciudad" del diccionario persona.
persona["ciudad"] = "Medellin"

# 7. Usa update() para modificar o añadir una clave llamada "email".
persona.update({"email": "elkin@mail.com"})

# 8. Agrega una nueva clave llamada "profesión" con valor "Desarrollador".
persona["profesion"] = "Desarrollador"

# 9. Usa setdefault() para añadir la clave "estado_civil" con valor "union libre".
persona.setdefault("estado_civil", "union libre")

# =====================================================
# SECCIÓN 3: Eliminación de datos
# =====================================================

# 10. Usa pop() para eliminar la clave "edad" del diccionario persona.
persona.pop("edad")

# 11. Usa popitem() para eliminar el último elemento insertado.
persona.popitem()

# 12. Usa del para eliminar la clave "nombre".
del persona["nombre"]

# 13. Usa clear() para vaciar el diccionario.
persona.clear()

# =====================================================
# SECCIÓN 4: Recorrido de diccionarios
# =====================================================
persona = {
    "nombre": "elkin",
    "edad": 27,
    "trabaja": True,
    "pasatiempos": ["estudiar", "gym", "musica"],
}

# 14. Recorre un diccionario imprimiendo solo las claves.
for claves in persona:
    print(claves)

# 15. Recorre un diccionario imprimiendo solo los valores.
for valores in persona.values():
    print(valores)

# 16. Recorre un diccionario imprimiendo clave y valor usando items().
for claves, valores in persona.items():
    print(f"{claves} : {valores}")

# =====================================================
# SECCIÓN 5: Copia de diccionarios
# =====================================================

# 17. Crea una copia de un diccionario usando copy().
print(id(persona))
persona1 = persona.copy()
print(id(persona1))

# 18. Crea una copia usando dict() y verifica que es independiente del original.
persona2 = dict(persona)
print(id(persona2))

# Extra
persona3 = {**persona}
print(id(persona3))

# =====================================================
# SECCIÓN 6: Diccionarios anidados
# =====================================================

# 19. Crea un diccionario llamado estudiantes con tres estudiantes. Cada uno debe tener nombre, edad y notas (lista).
estudiantes = {
    "Juan": {"edad": 22, "notas": [4.5, 3.0, 5.0, 2.5]},
    "Maria": {"edad": 18, "notas": [3.5, 3.0, 3.0, 1.5]},
    "Carlos": {"edad": 21, "notas": [4.5, 2.0, 4.0, 1.0]},
}

# 20. Crea un diccionario con 2 personas, donde cada persona tiene un subdiccionario con dirección y teléfono.
personas = {
    "Jose": {"direccion": "calle 26 sur 1-20", "telefono": "86790832"},
    "Laura": {"direccion": "cra 17a 2-31", "telefono": "90785432"},
}

# 21. Recorre un diccionario anidado mostrando los datos de cada persona formateados.
for nombre_persona, atributos_persona in personas.items():
    print(f"{nombre_persona}: ")
    for atributo, valor in atributos_persona.items():
        print(f"{' ' * 4} {atributo.capitalize()}: {valor.lower()}")

# 22. Accede al segundo elemento de la lista "notas" del segundo estudiante.
print(estudiantes["Maria"]["notas"])

# =====================================================
# SECCIÓN 7: Aplicaciones prácticas
# =====================================================

# 23. Crea un programa que reciba información de contacto de varias personas (nombre, teléfono, email) y la almacene en un diccionario.
agenda = []

while True:
    nombre = input("Ingresa el nombre: ")
    if not nombre.isalpha():
        print("Nombre incorrecto. Intenta de nuevo.")
        continue

    telefono = input("Ingresa el teléfono: ")
    if not telefono.isdigit():
        print("Debes ingresar solo números para el teléfono.")
        continue

    email = input("Ingresa el email: ")
    if not (
        "@" in email and email.index("@") > 0 and email.index("@") < len(email) - 1
    ):
        print("El email ingresado debe contener '@' con texto antes y después.")
        continue

    persona = {"nombre": nombre, "telefono": telefono, "email": email}
    agenda.append(persona)

    continuar = input("¿Deseas ingresar otra persona? (s/n): ")
    if continuar.lower() != "s":
        break

print("Agenda completa:")
for persona in agenda:
    print(persona)

# 24. Crea una agenda con nombres como claves y lista de hobbies como valor. Imprime todos los hobbies de "Laura".

# 25. Simula el historial de servicios de un auto como una lista de diccionarios dentro del diccionario del auto.

# 26. Dado un diccionario de productos con su stock, actualiza el stock de un producto específico luego de una compra.

# 27. Crea una función que reciba un diccionario y devuelva una lista con todas las claves que tengan valores tipo lista.

# 28. Crea un diccionario que represente una factura: cliente, productos (lista), total. Recorre el diccionario e imprime la factura.

# 29. Usa fromkeys() para crear un diccionario con claves ["a", "b", "c"] y el mismo valor 0.

# 30. Usa comprensión de diccionarios para crear un nuevo diccionario con claves del 1 al 5 y valores al cuadrado.
