def reorganizar_y_filtrar(numeros, S):


    numeros_filtrados = []

    for numero in numeros:


        numero_str = str(numero)
        numero_filtrado_str = ""

        for caracter_digito in numero_str:


            digito = int(caracter_digito)

            if digito < S:

                numero_filtrado_str += caracter_digito

        if numero_filtrado_str:

            numeros_filtrados.append(int(numero_filtrado_str))


    resultado = sorted(numeros_filtrados, reverse=True)

    return resultado



print(reorganizar_y_filtrar([1, 2, 3, 4, 5, 6], 8))  # [6, 5, 4, 3, 2, 1]
print(reorganizar_y_filtrar([10, 20, 30, 40], 8))  # [40, 30, 20, 10]
print(reorganizar_y_filtrar([6], 8))  # [6]
print(reorganizar_y_filtrar([66], 8))  # [6]
print(reorganizar_y_filtrar([65], 8))  # [5]
print(reorganizar_y_filtrar([6, 2, 1], 8))  # [6, 2, 1]
print(reorganizar_y_filtrar([60, 6, 5, 4, 3, 2, 7, 7, 29, 1], 8))  # [7, 7, 6, 5, 4, 3, 2, 2, 1]
