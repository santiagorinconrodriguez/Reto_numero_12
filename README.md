## Reto n° 12
### Nombre: Brayan Santiago Rincón Rodríguez
### Curso: Programación de computadores

### 1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
 ``` python 
# Iniciamos el programa creando un diccionario que contienen su respectiva clave y valor
mi_diccionario = {
    'code': 0,
    'craft': 9,
    'busca': 7,
    'minas': 4
}

# Extraemos los valores y los ordenamos de forma ascendente con sorted
valores_ordenados = sorted(mi_diccionario.values())

# Imprimimos los valores de forma ordenada recorriendolos con un ciclo for
print("Valores ordenados de forma ascendente:")
for valor in valores_ordenados:
    print(valor)
 ```

### 2. Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

 ``` python 
# Se define una función, a la cual le entran dos diccionarios y retorna otro como la mezcla de los mismos
def mezclar_diccionarios(dic1, dic2):
    mezcla = dic1.copy()  # Se copia el primer diccionario para no modificarlo, ya que estos son mutables

    # Con ayuda de un ciclo for recorremos las claves y los valores del segundo diccionario
    for clave, valor in dic2.items():
        # Si alguna clave del diccionario 2 no está en el diccionario mezcla (copia del diccionario 1), lo añade
        if clave not in mezcla:
            mezcla[clave] = valor

    # Al final retorna el nuevo diccionario con la mezcla de los dos
    return mezcla

# Se define otra función la cuál nos ayudará a ordenar los elementos de los tres diccionarios de forma ascendente
def mostrar_valores_ordenados(dic):
    valores = list(dic.values())  # Obtenemos todos los valores del diccionario evaluado
    valores_ordenados = sorted(valores)  # Ahora, los ordenamos alfabéticamente gracias al sorted

    # Finalmente, los imprimimos recorreindolos con el ciclo for
    print("Valores ordenados ascendentemente:")
    for valor in valores_ordenados:
        print(valor)

# Se le indica al programa que lo siguiente será la operación principal del código
if __name__ == "__main__":

    # Definimos dos diccionarios, un elemento con una misma clave para abarcar las condiciones del ejercicio
    dic1 = {
        "a": "10",
        "b": "20",
        "c": "30"
    }

    dic2 = {
        "b": "200",
        "d": "400",
        "e": "500"
    }
    
    # Imprimimos los dos diccionarios
    print("Primer diccionario:", dic1)
    print("Segundo diccionario:", dic2)

    # Mostramos los valores de los diccionarios de forma ordenada llamando a la función mostrar_valores_ordenados
    print("\nValores del primer diccionario ordenados:")
    mostrar_valores_ordenados(dic1)

    # Mezclamos los diccionarios llamando a la función mezclar_diccionarios
    dic_mezclado = mezclar_diccionarios(dic1, dic2)

    # Finalmente imprimimos el diccionario mezclado
    print("\nDiccionario mezclado:")
    print(dic_mezclado)
 ``` 

### 3. Cree un programa que lea de un archivo con el JSON dado y:

### Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
### Imprima los nombres completos (nombre y apellidos) de las personas que estén en un rango de edades dado por el usuario.

 ``` python
# Se importa el archivo json ya guardado en el mismo folder
import json

# Se procede a cargar este mismo archivo llamado punto_3.json y Se convierte el contenido json a un diccionario de Python
readFile = open('punto_3.json', "r", encoding='utf-8')
datos = json.load(readFile)  
readFile.close()

# Se le pide al usuario que ingrese un deporte para buscar en el Json
buscar_deporte = input("Ingrese el deporte a buscar (Primera letra mayúscula): ")

# Antes de buscarlo, se muestra el siguiente mensaje con un print
print("\nPersonas que practican", buscar_deporte, ":")
# Se le dice al proframa que recorra la clave-valor en cada uno de los datos del json
for usuario, info in datos.items():
    # Si el deporte está en un valor del json, se entrará en esta selección
    if buscar_deporte in info["deportes"]:
        # Una vez encontrado el deporte, se accede al nombre y apellido de la persona a la que le corresponde dicho deporte
        nombre_completo = info["nombres"] + " " + info["apellidos"]
        # Se imprime el nombre completo
        print(nombre_completo)

# Ahora se le pide al usuario un rango de edad
edad_min = int(input("Ingrese edad mínima: "))
edad_max = int(input("Ingrese edad máxima: "))

# Antes de buscarl las edades, se muestra el siguiente mensaje con un print
print("\nPersonas con edades entre", edad_min, "y", edad_max, ":")
# Se le dice al proframa que recorra la clave-valor en cada uno de los datos del json
for usuario, info in datos.items():
     # Si la edad está entre uno de los rangos establecidos por el usuario, se entrará en esta selección
    if edad_min <= info["edad"] <= edad_max:
        # Una vez encontrado el rango de las edades, se accede al nombre y apellido de la persona a la que le corresponde dicha edad
        nombre_completo = info["nombres"] + " " + info["apellidos"]
        # Se imprime el nombre completo
        print("-", nombre_completo)
 ``` 

### 4. A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.

 ``` python
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
# Este está interesante :)
nombre = input ("Ingrese un nombre en minuscula: ")
url3 = f"https://api.agify.io/?name={nombre}"
response3 = requests.get(url3)
data3 = response3.json()

print("\n API 3: Agify ")
print(json.dumps(data3, indent=2))
print("\nPares clave:valor")
for clave, valor in data3.items():
    print(clave, ":", valor)
  ``` 


### 5. Revise los campos (Para el JSON con el pronostivo detallado del clima para 8 días): 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.

  ``` python
import json
from datetime import datetime

jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)

# Campos de alerta y variable relevante
alertas = {
    'alertPrecip': 'prcp',
    'alertVelViento': 'velViento',
    'alertTmpMax': 'tmpMax',
    'alertTmpMin': 'tmpMin',
    'alertAlertas': None  # solo alerta, no variable asociada
}

# Recorremos días 0..7
for i in range(8):
    fecha_unix = data['dt'][str(i)]
    fecha_legible = datetime.utcfromtimestamp(fecha_unix).strftime('%Y-%m-%d')
    
    for campo_alerta, campo_valor in alertas.items():
        valor_alerta = data[campo_alerta][str(i)]
        
        if valor_alerta == "X":
            print(f"\n Alerta detectada:")
            print(f"   Fecha: {fecha_legible}")
            print(f"   Tipo de alerta: {campo_alerta}")
            
            if campo_valor:
                valor_asociado = data[campo_valor][str(i)]
                print(f"   Valor asociado ({campo_valor}): {valor_asociado}")
 ``` 
### Nombre: Brayan Santiago Rincón Rodríguez
### Curso: Programación de computadores