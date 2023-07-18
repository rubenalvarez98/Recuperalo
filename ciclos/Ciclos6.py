print("patron del triangulo")
altura = int(input("Ingrese la altura del triángulo: "))

for i in range(altura):
    print("*" * (i + 1))

for i in range(altura - 1):
    print("*" * (altura - i - 1))