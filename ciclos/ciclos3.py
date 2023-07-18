n = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea mostrar: "))

# Inicializar los primeros dos términos de la secuencia
termino1 = 0
termino2 = 1

# Mostrar los n términos de la secuencia y calcular la suma
suma = 0
print("Secuencia de Fibonacci:")
for i in range(n):
    print(termino1, end=" ")
    suma += termino1
    siguiente_termino = termino1 + termino2
    termino1 = termino2
    termino2 = siguiente_termino

print("\nSuma de los términos:", suma)
