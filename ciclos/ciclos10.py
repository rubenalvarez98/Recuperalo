# Imprimir la parte superior del patrón
for i in range(5):
    print("*", end="")
print()

# Imprimir la diagonal del patrón
for i in range(3):
    for j in range(3 - i):
        print(" ", end="")
    print("*")

# Imprimir la parte inferior del patrón
for i in range(5):
    print("*", end="")
print()
