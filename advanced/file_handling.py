# Tema: Manejo de archivos
""" 
La función clave para trabajar con archivos en Python es la open() función.
El open() La función toma dos parámetros; nombre de archivo, y modo.
 """
# "r" - Leer - Valor predeterminado. Abre un archivo para leer, devuelve un error si el archivo no existe
# "a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
# "w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
# "x" - Crear - Crea el archivo especificado, devuelve un error si el archivo existe
# "t" - Texto - Valor predeterminado. Modo texto
# "b" - Binario - Modo binario (por ejemplo, imágenes)

import xml.etree.ElementTree as ET
import xlrd
import csv
import json
file = open("files/reading_file_example.txt", "r")
txt = file.read()
print(type(txt))
print(txt)
file.close()

# Imprimir solo los 10 primeros caracteres
file = open("files/reading_file_example.txt", "r")
print(file.read(10))
file.close()


# readline(), lee sólo la primera linea
file = open("files/reading_file_example.txt", "r")
print(file.readline())
file.close()

# readlines(), lee todo el texto linea por línea y devuelve una lista de líneas
file = open("files/reading_file_example.txt", "r")
print(file.readlines())
file.close()

# Otra forma de obtener todas la líneas es usando splitlines()
file = open("files/reading_file_example.txt", "r")
lines = file.read().splitlines()
print(type(lines))
print(lines)
file.close()

# Después de abrir un archivo siempre se debe cerrar para evitar afectaciones sobre cambios en el archivos y en el buffer, esto se puedo olvidar para lo cual existe una alternativa que abre el archivo y lo cierra después de su uso como lo es with seguido de open()

with open("files/reading_file_example.txt", "r") as file:
    lines = file.read().splitlines()
    print(type(lines))
    print(lines)


# Abrir archivos para escribirlos y actualizarlos
# "a" - agregar - se agregará al final del archivo, si el archivo no lo hace, crea un nuevo archivo.
# "w" - escribir - sobrescribirá cualquier contenido existente, si el archivo no existe, lo crea.

with open("files/reading_file_example.txt", "a") as file:
    file.write("\nThis text has to be appended at the end")

with open("files/reading_file_example.txt", "r") as file:
    file = file.read()
    print(file)

# Eliminar Archivos
# print()
# import os
# os.remove('files/reading_file_example.txt')

# # Eliminación segura
# path = "files/reading_file_example.txt"
# if os.path.exists(path):
#    os.remove(path)
# else:
#     print("The file does not exist")


# Tipos de archivos
# json
# Ejemplo
# dictionary
person_dct = {
    "name": "Elkin",
    "country": "Colombia",
    "city": "Soacha",
    "skills": ["JavaScrip", "React", "Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Elkin', 'country': 'Colombia', 'city': 'Soacha', 'skills': ['SQL', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Elkin",
    "country":"Colombia",
    "city":"Soacha",
    "skills":["SQL", "Python"]
}'''

# Cambiar JSON a diccionario

# JSON
person_json = '''{
    "name":"Elkin",
    "country":"Colombia",
    "city":"Soacha",
    "skills":["SQL", "Python"]
}'''

# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Cambiar diccionario a JSON
person = {
    "name": "Elkin",
    "country": "Colombia",
    "city": "Soacha",
    "skills": ["SQL", "Python"]
}

person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)

# Guardar como archivo JSON
with open("files/json_example.txt", "w", encoding="utf-8") as file:
    json.dump(person, file, ensure_ascii=False, indent=4)

# Archivo con extensión csv
with open("files/csv_example.csv") as file:
    csv_reader = csv.reader(file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are: {','.join(row)}")
            line_count += 1
        else:
            print(f"\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}")
            line_count += 1
    print(f"Number of lines: {line_count}")

# Archivo con extensión xlsx
excel_book = xlrd.open_workbook("files/sample.xls")
print(excel_book.nsheets)
print(excel_book.sheet_names())

# Archivo con extensión xml

tree = ET.parse("files/xml_example.xml")
root = tree.getroot()
print("Root tag:", root.tag)
print("Attribute:", root.attrib)
for child in root:
    print("field:", child.tag)
