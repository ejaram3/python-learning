# =====================================================
# SECCIÓN 1: Sintaxis básica y asignación
# =====================================================

# 1. Crea una variable llamada nombre y asígnale tu nombre. Imprímela.
name = "Elkin"

# 2. Crea dos variables llamadas a y b. Asígnales valores numéricos e imprime su suma, resta y multiplicación.
a = 3
b = 5
print(a + b)
print(a - b)
print(a * b)

# 3. Crea una variable llamada es_estudiante y asígnale el valor True. Imprime un mensaje como: "¿Eres estudiante? True"
is_student = True
print(f"¿Eres estudiante? {is_student}")

# 4. Crea una variable llamada mensaje y asígnale un texto. Luego cambia su valor por otro texto e imprímelo.
message = "Hola mundo"
message = "Python"
print(message)

# 5. Crea una variable año_actual con el valor 2025 y otra con tu año de nacimiento. Calcula tu edad y guárdala en una variable edad.
current_year = 2025
current_of_birth = 1997
my_age = current_year - current_of_birth
print(my_age)

# 6. Usa f-strings para mostrar un mensaje como: "Juan tiene 20 años y vive en Medellín".

name = "Juan"
age = 20
city = "Medellin" 
message = f"{name} tiene {age} años y vive en {city}"
print(message)

# =====================================================
# SECCIÓN 2: Operaciones con variables
# =====================================================

# 7. Crea tres variables: producto, precio_unitario y cantidad. Calcula el total a pagar e imprímelo con f-string.
product = 'pc'
unit_price = 3213
quantity = 3
calculation = unit_price * quantity
print(f"El precio del {product} es de USD {calculation}")

# 8. Declara dos variables numéricas y realiza una división. Imprime también el resultado como número redondeado a 2 decimales.
first_variable = 2432
second_variable = 52
print(f"Resultado de la division es de {(first_variable/second_variable):.2f}")

# 9. Declara una variable llamada nombre_completo y otra llamada iniciales. Iniciales debe contener solo la primera letra del nombre y apellido (ej: "Carlos Ruiz" → "CR").
name_employment = 'Ingeniero de datos'
initials = 'EJ'

# 10. Crea una variable que almacene el resultado de convertir una temperatura de Celsius a Fahrenheit. Fórmula: `F = C * 1.8 + 32`
celsius = 90
fahrenheit = celsius * 1.8 + 32


# =====================================================
# SECCIÓN 3: Buenas prácticas y errores comunes
# =====================================================

# 11. Crea una variable con un nombre que siga las buenas prácticas (snake_case) y otra con mal nombre. Observa la diferencia.
first_variable = 1 
# 1variable = 1 

# 12. Intenta usar una variable que no ha sido definida. ¿Qué error aparece?
# suma = value_1 + 2 # NameError
# print(suma)

# 13. Declara dos variables: edad y Edad. Asígnales valores distintos e imprime ambos. ¿Qué observas?
age = 23
Age = 28

# 14. Usa una palabra reservada como nombre de variable (por ejemplo, def, list, str). ¿Qué ocurre?
# def = 7 # SyntaxError

# =====================================================
# SECCIÓN 4: Mini desafíos prácticos
# =====================================================

# 15. Crea un pequeño programa que calcule el área de un triángulo usando base y altura almacenadas en variables.

# 16. Pide al usuario (usando input) su nombre y edad, y guarda ambos en variables. Imprime un mensaje usando f-string.

# 17. Simula una pequeña tienda: declara variables para 3 productos (nombre, precio y cantidad). Calcula y muestra el total.

# 18. Crea una variable llamada saldo_inicial con un valor. Luego crea otra llamada gasto. Resta gasto a saldo_inicial y guarda el resultado en saldo_actual.

# 19. Declara variables para nombre de usuario, contraseña y email. Imprímelas en una sola línea separadas por guiones.

# 20. Define variables con tus hobbies favoritos y concaténalos en una sola cadena con comas.
