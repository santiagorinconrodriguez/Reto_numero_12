
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
