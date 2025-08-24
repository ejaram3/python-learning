# Escriba una función que cuente el número de líneas y el número de palabras en un texto. Todos los archivos están en la carpeta de datos:
#  a) Lea el archivo obama_speech.txt y cuente el número de líneas y palabras
#  b) Lea el archivo michelle_obama_speech.txt y cuente el número de líneas y palabras
#  c) Lea el archivo donald_speech.txt y cuente el número de líneas y palabras
#  d) Lea el archivo melina_trump_speech.txt y cuente el número de líneas y palabras
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import csv
from collections import Counter
import json
import re


def n_lines_and_words(path_file: str) -> str:
    with open(path_file, "r", encoding="utf-8") as f:
        full_text = f.read()

    lines = full_text.splitlines()
    num_lines = len(lines)

    regex_pattern = r"\w+"
    words = re.findall(regex_pattern, full_text.lower())
    num_words = len(words)

    return f"Archivo: {path_file.split('/')[-1]}\nNumero de lineas: {num_lines}\nNumero de palabras: {num_words}\n"


# print(n_lines_and_words("../files/obama_speech.txt"))
# print(n_lines_and_words("../files/michelle_obama_speech.txt"))
# print(n_lines_and_words("../files/donald_speech.txt"))
# print(n_lines_and_words("../files/melina_trump_speech.txt"))

# Lea el archivo de datos countries_data.json en el directorio de datos, cree una función que encuentre los diez idiomas más hablados


def top_languages(file_path: str, top_n: int = 10) -> list[tuple[str, int]]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    language_counter = Counter()

    for country in data:
        languages = country.get("languages", [])
        seen = set()
        for lang in languages:
            if isinstance(lang, dict):
                lang_name = lang.get("name")
            elif isinstance(lang, str):
                lang_name = lang
            else:
                continue

            if lang_name and lang_name not in seen:
                language_counter[lang_name] += 1
                seen.add(lang_name)

    return language_counter.most_common(top_n)


# print(top_languages("../files/countries_data.json"))

# Lea el archivo de datos countries_data.json en el directorio de datos, cree una función que cree una lista de los diez países más poblados


def most_populated_countries(file_path: str, top_n: int = 10):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    countries_with_population = [
        (country["name"], country.get("population", 0))
        for country in data
        if "population" in country and isinstance(country["population"], (int, float))
    ]

    sorted_countries = sorted(
        countries_with_population,
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_countries[:top_n]


# print(most_populated_countries("../files/countries_data.json"))

# Extraiga todas las direcciones de correo electrónico entrantes como una lista del archivo email_exchange_big.txt.

# EMAIL_REGEX = re.compile(
#     r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}\b'
# )

# INPUT_FILE  = Path("../files/email_exchanges_big.txt")
# OUTPUT_FILE = Path("../files/list_emails.csv")


# with INPUT_FILE.open("r", encoding="utf-8") as f:
#     txt = f.read()

# raw_emails = EMAIL_REGEX.findall(txt)

# unique_emails = sorted(set(raw_emails))

# print(f"Se encontraron {len(raw_emails)} correos, "
#       f"{len(unique_emails)} únicos después de deduplicar.")

# with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(["Email"])
#     writer.writerows([[email] for email in unique_emails])

# print(f"Lista de correos guardada en: {OUTPUT_FILE}")

# Encuentra las palabras más comunes en el idioma inglés. Llame al nombre de su función find_most_common_words, tomará dos parámetros: una cadena o un archivo y un número entero positivo, que indica el número de palabras. Su función devolverá una matriz de tuplas en orden descendente. Verifique la salida
def find_most_common_words(path_file, n_words):
    WORDS_REGEX = re.compile(r"\b[a-zA-Z]+\b")

    INPUT_FILE = Path(path_file)

    with INPUT_FILE.open("r", encoding="utf-8") as f:
        txt = f.read()

    raw_words = WORDS_REGEX.findall(txt)

    counter_words = Counter()

    for item in raw_words:
        words = item.lower().split()
        for word in words:
            counter_words[word] += 1

    return counter_words.most_common(n_words)


print(find_most_common_words("../files/obama_speech.txt", 10))

# Utilice la función find_most_frequent_words para encontrar:
# a) Las diez palabras más frecuentes utilizadas en El discurso de Obama
# b) Las diez palabras más frecuentes utilizadas en El discurso de Michelle
# c) Las diez palabras más frecuentes utilizadas en El discurso de Trump
# d) Las diez palabras más frecuentes utilizadas en El discurso de Melina
print(find_most_common_words("../files/obama_speech.txt", 10))
print(find_most_common_words("../files/michelle_obama_speech.txt", 10))
print(find_most_common_words("../files/melina_trump_speech.txt", 10))

# Escriba una aplicación de Python que verifique la similitud entre dos textos. Toma un archivo o una cadena como parámetro y evaluará la similitud de los dos textos. Por ejemplo, verifique la similitud entre las transcripciones de De Michelle y De Melina discurso. Es posible que necesite un par de funciones: función para limpiar el texto (clean_text), función para eliminar palabras de soporte (remove_support_words) y, finalmente, para verificar la similitud (check_text_similarity). Lista de detener palabras están en el directorio de datos

# Configuración

# Descargar stopwords solo si no están presentes
nltk.download('stopwords', quiet=True)

# Lista de stopwords en español
STOPWORDS_ES = set(stopwords.words('spanish'))

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Utilidades

def read_file(filename: str, folder: str = "files") -> str:
    """
    Lee un archivo de texto desde el directorio especificado.
    """
    path_file = BASE_DIR / folder / filename
    with open(path_file, "r", encoding="utf-8") as f:
        return f.read()


def clean_text(text: str) -> str:
    """
    Convierte a minúsculas, elimina caracteres especiales y espacios extra.
    """
    text = text.lower()
    text = re.sub(r'[^a-záéíóúñü0-9\s]+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def remove_support_words(texto: str) -> str:
    """
    Elimina stopwords manteniendo la puntuación.
    """
    tokens = re.findall(r'\b\w+\b|[^\w\s]', texto, re.UNICODE)
    palabras_filtradas = [
        token for token in tokens
        if token.lower() not in STOPWORDS_ES or not token.isalpha()
    ]

    resultado = []
    for i, token in enumerate(palabras_filtradas):
        if i > 0 and token.isalnum() and resultado[-1].isalnum():
            resultado.append(' ')
        resultado.append(token)

    return ''.join(resultado)


# Lógica principal

def check_text_similarity(text1: str, text2: str) -> float:
    """
    Calcula la similitud entre dos textos usando TF-IDF y similitud coseno.
    Retorna un valor entre 0 y 1.
    """
    # Limpieza y filtrado
    text1_clean = remove_support_words(clean_text(text1))
    text2_clean = remove_support_words(clean_text(text2))

    # Vectorización y cálculo de similitud
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1_clean, text2_clean])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity, 4)


def orquestador(name_text: str, fun=clean_text) -> str:
    """
    Orquesta lectura, limpieza y eliminación de stopwords.
    """
    raw_text = read_file(name_text)
    cleaned_text = fun(raw_text)
    filtered_text = remove_support_words(cleaned_text)
    return filtered_text


# Ejecución directa

if __name__ == "__main__":
    texto_a = read_file("michelle_obama_speech.txt")
    texto_b = read_file("melina_trump_speech.txt")

    score = check_text_similarity(texto_a, texto_b)
    print(f"Similitud: {score}")

# Encuentra las 10 palabras más repetidas en romeo_and_juliet.txt

# Lea el noticias de hackers csv archiva y descubre:
    # a) Cuente el número de líneas que contienen Python o Python
    # b) Cuente las líneas numéricas que contienen JavaScript, javascript o Javascript
    # c) Cuente las líneas numéricas que contienen Java y no JavaScript


def counter_words(word, file):
    path_file = BASE_DIR / "files" / file

    # Compilar regex según el caso
    if word.lower() == "python":
        pattern = re.compile(r"\bpython\b", re.IGNORECASE)
    elif word.lower() == "javascript":
        pattern = re.compile(r"\bjavascript\b", re.IGNORECASE)
    elif word.lower() == "java":
        # Java pero que no esté seguido de 'script'
        pattern = re.compile(r"\bjava\b(?!script)", re.IGNORECASE)
    else:
        pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)

    count = 0
    with open(path_file, "r", encoding="utf-8") as f:
        csv_reader = csv.reader(f, delimiter=",")
        next(csv_reader)  # saltar header si existe

        for row in csv_reader:
            text = row[1]
            if pattern.search(text):
                count += 1

    return count


print("Python:", counter_words("Python", "hacker_news.csv"))
print("JavaScript:", counter_words("JavaScript", "hacker_news.csv"))
print("Java:", counter_words("Java", "hacker_news.csv"))
