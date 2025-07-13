import requests # Se importa request, el cual nos permitirá pedir información a una url
import json # Posteriormente, Se importa json para mostrar de forma legible la respuesta JSON

# API 1: Cat Fact. Se define la URL de la API
url1 = "https://catfact.ninja/fact"
response1 = requests.get(url1)
data1 = response1.json()

print("\n API 1: Cat Fact")
# Se convierte la respuesta a formato JSON (diccionario de Python)
print(json.dumps(data1, indent=2))

# Se imprime el siguiente mensaje
print("\nPares clave:valor")
# Se recorren los pares clave valor para cada uno de los elementos del API, imprimiendo los mismos durante cada iteración
for clave, valor in data1.items():
    print(clave, ":", valor)

# API 2: Kanye Rest
url2 = "https://api.kanye.rest"
response2 = requests.get(url2)
data2 = response2.json()

print("\n API 2: Kanye Quote")
print(json.dumps(data2, indent=2))

print("\nPares clave:valor")
for clave, valor in data2.items():
    print(clave, ":", valor)

# API 3: Agify (predice edad por nombre)
# Este está interesante
nombre = input ("Ingrese un nombre en minuscula: ")
url3 = f"https://api.agify.io/?name={nombre}"
response3 = requests.get(url3)
data3 = response3.json()

print("\n API 3: Agify ")
print(json.dumps(data3, indent=2))
print("\nPares clave:valor")
for clave, valor in data3.items():
    print(clave, ":", valor)