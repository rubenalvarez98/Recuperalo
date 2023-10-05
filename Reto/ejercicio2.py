def cuadrados_ordenados(array):

    S = 88


    cuadrados_validos = [] #array vacio para almacenar


    for numero in array: #recorrer el array

        cuadrado = numero * numero  #cuadrado del numero


        if 0 <= cuadrado <= S: #validar si esta en el rango

            cuadrados_validos.append(cuadrado) # agregar a validos


    cuadrados_validos.sort() #se ordena sendentemente

    #
    return cuadrados_validos # lo que retorna la funcion



entrada_1 = [1, 2, 3, 5, 6, 8, 9]
resultado_1 = cuadrados_ordenados(entrada_1)
print(resultado_1)

entrada_2 = [-2, -1]
resultado_2 = cuadrados_ordenados(entrada_2)
print(resultado_2)

entrada_3 = [-6, -5, 0, 5, 6]
resultado_3 = cuadrados_ordenados(entrada_3)
print(resultado_3)

entrada_4 = [-10, 10]
resultado_4 = cuadrados_ordenados(entrada_4)
print(resultado_4)



