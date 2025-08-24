# Lee esta URL y encuentra las 10 palabras más frecuentes. romeo_and_juliet
import statistics as stats
import statistics
import json
import requests
import re
from tabulate import tabulate
from collections import Counter
url = "https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/romeo_and_juliet.txt"

response = requests.get(url)

if response.status_code == 200:
    text = response.text
    word_regex = r"\b[a-zA-Z]+\b"
    matches_text = re.findall(word_regex, text)
    conteo = Counter([w.lower() for w in matches_text])
    # print(conteo.most_common(10))
else:
    print(f"Error HTTP: {response.status_code}")

# Lea la API de gatos y cats_api = 'https://api.thecatapi.com/v1/breeds' y encuentra:
    # la desviación estándar mínima, máxima, media, mediana del peso de los gatos en unidades métricas.
    # la desviación estándar mínima, máxima, media, mediana de la esperanza de vida de los gatos en años.
    # Crea una tabla de frecuencias de país y raza de gatos

url_thecatapi = "https://api.thecatapi.com/v1/breeds"
response = requests.get(url_thecatapi)

if response.status_code == 200:
    data = response.json()
    desviaciones_peso = []
    desviaciones_esperanza_vida = []
    pais_raza_list = []

    for cat in data:
        # Peso
        pesos_str = cat["weight"]["metric"].split(" - ")
        pesos = [float(x) for x in pesos_str]
        desv_peso_std = stats.stdev(pesos) if len(pesos) > 1 else 0
        desviaciones_peso.append(desv_peso_std)

        # Esperanza de vida
        vida_str = cat["life_span"].split(" - ")
        vida = [float(x) for x in vida_str]
        desv_vida_std = stats.stdev(vida) if len(vida) > 1 else 0
        desviaciones_esperanza_vida.append(desv_vida_std)

        # País y raza
        pais = cat["origin"] if cat["origin"] else "Desconocido"
        raza = cat["id"]
        pais_raza_list.append((pais, raza))

    # Resumen desviaciones
    # print(f"{'-' * 29} Peso {'-' * 29}")
    # print("Desviación estándar peso mínima:", min(desviaciones_peso))
    # print("Desviación estándar peso máxima:", max(desviaciones_peso))
    # print("Desviación estándar peso media:", stats.mean(desviaciones_peso))
    # print("Desviación estándar peso mediana:", stats.median(desviaciones_peso))

    # print(f"{'-' * 22} Esperanza de vida {'-' * 22}")
    # print("Desviación estándar esperanza vida mínima:", min(desviaciones_esperanza_vida))
    # print("Desviación estándar esperanza vida máxima:", max(desviaciones_esperanza_vida))
    # print("Desviación estándar esperanza vida media:", stats.mean(desviaciones_esperanza_vida))
    # print("Desviación estándar esperanza vida mediana:", stats.median(desviaciones_esperanza_vida))

    # Tabla de frecuencia real (conteo por país y raza)
    conteo = Counter(pais_raza_list)
    tabla_frecuencia = [(pais, raza, freq)
                        for (pais, raza), freq in conteo.items()]

    # print(f"{'-' * 17} Tabla Frecuencia País, Raza {'-' * 17}")
    cabezera = ["Pais", "Raza", "Frecuencia"]
    # print(tabulate(tabla_frecuencia, headers=cabezera, tablefmt="grid"))

else:
    print(f"Error HTTP: {response.status_code}")


# Lea el API de países y encontrar
    # Los 10 países más grandes
    # Los 10 idiomas más hablados
    # el número total de idiomas en los países API
url_countries = "https://www.apicountries.com/countries"
response_api_countries = requests.get(url_countries)

if response_api_countries.status_code == 200:
    data_api_countries = response_api_countries.json()
    top_10_countries_big = []
    top_10_languages = []

    for country in data_api_countries:
        top_10_countries_big.append((country["name"], country.get("area", 0)))

        for lan in country.get("languages", []):
            top_10_languages.append(lan["name"])

    top_10_lan = Counter(top_10_languages)

    lst_sorted = sorted(top_10_countries_big, key=lambda x: x[1], reverse=True)
    print(f"Los 10 países más grandes del mundo:\n{lst_sorted[:10]}")
    print(
        f"\nLos 10 idiomas más hablados del mundo:\n{top_10_lan.most_common(10)}")
    print(
        f"\nNúmero total de idiomas en los países:\n{len(set(top_10_languages))}")
else:
    print(f"Error HTTP {response_api_countries.status_code}")



from bs4 import BeautifulSoup

# URL actualizada del repositorio de datasets
url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Buscar todos los enlaces de datasets (están en la tabla principal)
    table = soup.find("table", {"border": "1"})  # tabla con datasets
    dataset_names = []

    if table:
        rows = table.find_all("tr")[1:]  # saltar encabezado
        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 0:
                # El nombre del dataset está en la primera columna como enlace
                dataset_name = cols[0].get_text(strip=True)
                dataset_names.append(dataset_name)

    print(f"Se encontraron {len(dataset_names)} datasets")
    for name in dataset_names[:20]:  # mostrar primeros 20
        print(name)

else:
    print(f"Error HTTP {response.status_code}")