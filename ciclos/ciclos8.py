num = 1
for i in range(1, 6):  # Controla el número de filas
    for j in range(1, 6 - i):  # Imprime espacios en blanco
        print(" ", end="")

    for j in range(1, i + 1):  # Imprime números
        print(num, end=" ")
        num += 1
        if num > 10:  # Detiene la secuencia al llegar a 10
            break

    print()
