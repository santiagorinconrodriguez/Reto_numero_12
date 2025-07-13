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
