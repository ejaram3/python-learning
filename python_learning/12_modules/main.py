# Importar el módulo
import my_module
print(my_module.crea_nombre_completo("Carlos", "Perez"))

# Otra forma es importar la funciones especificas de ese modulo
from my_module import crea_nombre_completo, suma_dos_numeros, resta_dos_numeros, mult_dos_numeros, div_dos_numeros
print(crea_nombre_completo("Elkin", "Jaramillo"))
print(suma_dos_numeros(2, 3))
print(resta_dos_numeros(2, 3))
print(mult_dos_numeros(2, 3))
print(div_dos_numeros(2, 3))

# Importar funciones de un módulo y cambiar nombre
from my_module import crea_nombre_completo as n, suma_dos_numeros as s, resta_dos_numeros as r, mult_dos_numeros as m, div_dos_numeros as d

print(n("Samuel", "Martinez"))
print(s(7, 5))
print(r(7, 5))
print(m(7, 5))
print(d(7, 5))

# Importar módulos integrados
# Modulo OS
import os
path = "python_learning/12_modules/Prueba"
# # Creando un directorio
# os.mkdir(path)
# # Cambiar el directorio actual
# os.chdir(pth)
# # Obtener el directorio de trabajo actual
# print(os.getcwd())
# # Eliminando directorio
# os.rmdir(path)

# Modulo Sys

import sys
# # print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# # para salir del sistema
# sys.exit()
# # Para saber la variable entera más grande se necesita
# sys.maxsize()
# # Para conocer la ruta del entorno
# sys.path
# # Para conocer la version de python que se esta usando
# sys.version

# Módulo de estadísticas 
from statistics import *
edades = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(edades))
print(median(edades))
print(mode(edades))
print(stdev(edades))

# Módulo de matemáticas
from math import pi, sqrt, floor, ceil, log10
print(pi)
print(sqrt(9))
print(pow(2, 3))
print(floor(2.81))
print(ceil(2.81))
print(log10(100))

# Módulo string
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
 
# Módulo aleatorio
from random import random, randint
print(random())
print(randint(5, 20))
