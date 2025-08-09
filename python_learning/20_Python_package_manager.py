"""
TEMA: Python PIP – Administrador de Paquetes
PIP: Programa Instalador Preferido

# --- COMANDOS BÁSICOS ---
pip install nombre_paquete             # Instalar
pip uninstall nombre_paquete           # Desinstalar
pip list                               # Listar instalados
pip show nombre_paquete                # Info básica
pip show nombre_paquete --verbose      # Info detallada
pip freeze                             # Listar con versiones
pip freeze > requirements.txt          # Guardar dependencias

# --- USO AVANZADO ---
python -m pip install --upgrade pip    # Actualizar pip
pip install paquete==1.2.3             # Versión específica
pip install --upgrade paquete          # Actualizar paquete
pip install -r requirements.txt        # Instalar desde archivo
pip install https://url/paquete.zip    # Desde URL
pip install ./archivo.whl              # Desde archivo local
"""

# 1. Instalación de librerías
# Ejemplo: pip install numpy pandas requests
import pandas as pd
import numpy as np
import webbrowser
import requests

# 2. NumPy
lst = [1, 2, 3, 4, 5, 6, 7]
np_arr = np.array(lst)

# print(np_arr * 2)   # Multiplicación
# print(np_arr + 2)   # Suma
# print(len(np_arr))  # Longitud

# 3. Pandas
data = [
    ('id', '1'),
    ('name', "Juan"),
    ("age", 28)
]

df = pd.DataFrame(data)
# print(df)

# 4. webbrowser
# urls = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]
# for url in urls:
#     webbrowser.open_new_tab(url)

# 5. Requests

# Imagen desde URL
url_img = 'https://media.licdn.com/dms/image/v2/D4E03AQEK_ZUVb_ZPIA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1710358415825?e=2147483647&v=beta&t=CVAV7XVFbW0Nm7U1jY6CMf-t_Tqje3E1nwh63qQ5VXI'
response_img = requests.get(url_img)
# print(response_img.status_code, response_img.headers)

# API de GitHub
url_api = 'https://api.github.com/'
response_api = requests.get(url_api)
# print(response_api.status_code, response_api.json())


# Creación y llamado de un paquete en Python
from mypackage import arithmetics

print(arithmetics.add_numbers(1, 2, 3, 4, 5, 6, 7))
print(arithmetics.subtract(2, 5))
print(arithmetics.division(2, 3))
print(arithmetics.remainder(5, 6))
print(arithmetics.power(5, 6))

from mypackage import greet
print(greet.greet_person("Elkin", "Jaramillo"))