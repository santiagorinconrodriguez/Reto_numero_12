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