numeros = []

# Solicitar al usuario que ingrese los 5 números
for i in range(5):
    numero = float(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)

# Calcular la suma de los números
suma = 0
for numero in numeros:
    suma += numero

# Calcular el promedio
promedio = suma / len(numeros)

# Imprimir el resultado
print("El promedio de los números es:", promedio)