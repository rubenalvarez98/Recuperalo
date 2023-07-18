while True:
    print("Seleccione una figura geométrica:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Rombo")
    print("6. Trapecio")
    print("0. Salir")

    opcion = int(input("Ingrese el número de opción: "))

    if opcion == 0:
        break

    if opcion == 1:
        lado = float(input("Ingrese el valor del lado del cuadrado: "))
        area = lado ** 2
        print("El área del cuadrado es:", area)
    elif opcion == 2:
        base = float(input("Ingrese el valor de la base del rectángulo: "))
        altura = float(input("Ingrese el valor de la altura del rectángulo: "))
        area = base * altura
        print("El área del rectángulo es:", area)
    elif opcion == 3:
        base = float(input("Ingrese el valor de la base del triángulo: "))
        altura = float(input("Ingrese el valor de la altura del triángulo: "))
        area = (base * altura) / 2
        print("El área del triángulo es:", area)
    elif opcion == 4:
        radio = float(input("Ingrese el valor del radio del círculo: "))
        area = 3.1416 * (radio ** 2)
        print("El área del círculo es:", area)
    elif opcion == 5:
        diagonal_mayor = float(input("Ingrese el valor de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese el valor de la diagonal menor del rombo: "))
        area = (diagonal_mayor * diagonal_menor) / 2
        print("El área del rombo es:", area)
    elif opcion == 6:
        base_mayor = float(input("Ingrese el valor de la base mayor del trapecio: "))
        base_menor = float(input("Ingrese el valor de la base menor del trapecio: "))
        altura = float(input("Ingrese el valor de la altura del trapecio: "))
        area = ((base_mayor + base_menor) * altura) / 2
        print("El área del trapecio es:", area)
    else:
        print("Opción inválida. Intente nuevamente.")
