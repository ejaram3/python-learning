# Obtenga el día, el mes, el año, la hora, el minuto y la marca de tiempo actuales del módulo de fecha y hora
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}, {timestamp}")

# Formatee la fecha actual usando este formato: "%m/%d/%Y, %H:%M:%S")
f_datetime = datetime.strftime(now, "%m/%d/%Y, %H:%M:%S")
print(f_datetime)
# Hoy es 5 de diciembre de 2019. Cambia esta cadena de tiempo a tiempo.
string_date = "5 December, 2019"
change_date = datetime.strptime(string_date, "%d %B, %Y")
print(change_date)

# Calcula la diferencia horaria entre ahora y el año nuevo.

current_date = datetime.now()
new_year_date = datetime(2026, 1, 1)
diff = new_year_date - current_date
print("Tiempo restante para el Año Nuevo 2026:")
print(diff)

# Calcule la diferencia horaria entre el 1 de enero de 1970 y ahora.
before_date = datetime(1970, 1, 1)
current_date = datetime.now()
diff = current_date - before_date
print("Diferencia horaria desde 01 enero 1970 hasta hoy:")
print(diff)

# Piensa, ¿para qué puedes usar el módulo de fecha y hora? Ejemplos:
    # Análisis de series temporales
    # Para obtener una marca de tiempo de cualquier actividad en una aplicación
    # Agregar publicaciones en un blog
