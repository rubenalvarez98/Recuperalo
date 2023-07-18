numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Comparar los números para determinar el mayor y el menor
if numero1 > numero2:
    mayor = numero1
    menor = numero2
elif numero2 > numero1:
    mayor = numero2
    menor = numero1
else:
    print("Los números son iguales.")
    exit()

print("El número mayor es:", mayor)
print("El número menor es:", menor)
