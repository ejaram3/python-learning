# Tema: Datetime (Fecha y hora en python)
""" 
Este es un modulo con el que cuenta python para manejar la fecha y hora
"""

from datetime import timedelta
from datetime import time
from datetime import date
from datetime import datetime

# Obteniendo información de fecha y hora
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formato de la salida de la fecha usando strftime
new_year = datetime(2025, 1, 1)
print(new_year)

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formato de fecha usando strftime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time_one)
time_two = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_two)

# Creando a tiempo strptime
date_string = "5 December, 2025"
t = datetime.strptime(date_string, "%d %B, %Y")
print(t)

date_string_two = "03 August, 25"
t2 = datetime.strptime(date_string_two, "%d %B, %y")
print(t2)

# Usando fecha de fecha y hora
d = date(2025, 1, 1)
print(d)
print(f"Fecha actual: {d.today()}")
today = d.today()
print("dia:", today.day)
print("mes:", today.month)
print("año:", today.year)

# Objetos de tiempo para representar el tiempo
a = time()
print(a)

b = time(10, 20, 50)
print(b)

c = time(minute=30, second=59, hour=11)
print(c)

d = time(12, 34, 55, 200312)
print(d)

# Diferencia entre dos puntos en el tiempo
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print(diff)

# Diferencia entre dos puntos en el tiempo usando timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print(t3)
