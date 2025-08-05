import re
# ¿Cuál es la palabra más frecuente en el siguiente párrafo?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

regex_pattern = r"\w+"
matches = re.findall(regex_pattern, paragraph.lower())

count = {}
for word in matches:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True)

print(f"Palabras más frecuentes:")
for word, freq in sorted_counts:
    print((freq, word))

print()
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

regex_pattern = r"[-+]?\d+"
points = re.findall(regex_pattern, txt)
print(points)

integer_values = [int(x) for x in points]
sorted_points = sorted(integer_values)
print(sorted_points)

distance = max(sorted_points) - min(sorted_points)
print(distance)

# Escriba un patrón que identifique si una cadena es una variable válida de Python
# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True


def is_valid_variable(name_variable):
    regex_pattern = r'^[a-zA-Z_]\w*$'
    return re.match(regex_pattern, name_variable) is not None


print(is_valid_variable('firstname'))

# Limpia el siguiente texto. Después de limpiar, cuente las tres palabras más frecuentes en la cadena.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(txt):
    regex_pattern = r"[^\w\s]"
    clean_text = re.sub(regex_pattern, '', txt)
    if clean_text:
        return clean_text
    return None


print(clean_text(sentence))

txt = clean_text(sentence)


def most_frequent_words(txt):
    regex_pattern = r"\w+"
    matches = re.findall(regex_pattern, txt)

    count = {}
    for word in matches:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    sorted_counts = sorted(
        count.items(), key=lambda item: item[1], reverse=True)
    top_words = []
    for word, freq in sorted_counts[:3]:
        top_words.append((freq, word))
    return top_words


print(most_frequent_words(txt))
