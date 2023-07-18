numero = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1

# Verificar si el número es negativo, cero o positivo
if numero < 0:
    print("Solo numeros positivos")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        factorial *= i

    print("El factorial de", numero, "es", factorial)
