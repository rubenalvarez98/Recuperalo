print("tablas de multiplicar")
numero = int(input("Ingrese un número entero: "))

print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
