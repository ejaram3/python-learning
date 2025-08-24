# Tema: Expresiones regulares

""" 
Una expresión regular o RegEx es una cadena de texto especial que ayuda a encontrar patrones en los datos.
RegEx se puede usar para comprobar si existe algún patrón, se debe importar siempre el modulo de re 
"""
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md#regular-expressions

import re
# help(re)

# re.match(): busca solo en el comienzo de la primera línea de la cadena y devuelve objetos coincidentes si se encuentran, de lo contrario devuelve Ninguno.
# re.search: Devuelve un objeto de coincidencia si hay uno en cualquier lugar de la cadena, incluidas las cadenas de varias líneas.
# re.findall: Devuelve una lista que contiene todas las coincidencias
# re.split: Toma una cadena, la divide en los puntos de coincidencia, devuelve una lista
# re.sub: Reemplaza una o muchas coincidencias dentro de una cadena


# match()
txt = "I love to teach Python and Java"
match = re.match("I love to teach", txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

# search()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
search = re.search("first", txt, re.I)
print(search)

span = search.span()

start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

# findall()
findall = re.findall("python", txt, re.I)
print(findall)

findall = re.findall("language", txt, re.I)
print(findall)

# Forma si usar re.I
findall = re.findall("[P|p]ython", txt)
print(findall)

findall = re.findall("Python|python", txt)
print(findall)

# sub()
sub = re.sub("[P|p]ython", "Java", txt)
print(sub)

sub = re.sub("Python|python", "c#", txt)
print(sub)

print()
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
sub = re.sub("%", "", txt)
print(sub)

# Dividir un texto usando RegEx
# split()
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
split = re.split("\n", txt)
print(split)

# Como escribir patrones RegEx
regex_pattern = r"apple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)


matches = re.findall(regex_pattern, txt, re.I)
print(matches)

regex_pattern = r"[Aa]pple"
matches = re.findall(regex_pattern, txt)
print(matches)

print()
regex_pattern = r"[Aa]pple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"[Aa]pple|[Bb]anana"
matches = re.findall(regex_pattern, txt)
print(matches)

# Carácter escape (\)
regex_pattern = r"\d"
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# Una o mas veces (+)
regex_pattern = r"\d+"
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# Periodo (.)
regex_pattern = r"[Aa]."
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"[a].+"
matches = re.findall(regex_pattern, txt)
print(matches)

# Cero o más veces (*)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r"[Ee]-?mail"
matches = re.findall(regex_pattern, txt)
print(matches)

# Cuantificador en RegEx
# Podemos especificar una longitud de una subcadena que buscamos en un texto. Utilizando un corchete rizado. Imaginemos que nos interesa una subcadena con una longitud de 4 caracteres

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r"\d{4}"
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r"\d{1,4}"
matches = re.findall(regex_pattern, txt)
print(matches)

# Carro (ˆ) comienza con
regex_pattern = r"^This"
matches = re.findall(regex_pattern, txt)
print(matches)

# Negación
# El conjunto de caracteres significa negación y sin espacios
regex_pattern = r"[^A-Za-z ]+"
matches = re.findall(regex_pattern, txt)
print(matches)
