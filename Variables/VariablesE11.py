numero = float(input("Ingrese un número: "))

# Verificar si el número es negativo
if numero < 0:
    print("No se puede calcular la raíz cuadrada de un número negativo.")
else:
    # Estimación inicial de la raíz cuadrada
    raiz = numero / 2

    # Iterar hasta obtener una aproximación suficientemente precisa
    while abs(raiz * raiz - numero) > 0.0001:
        raiz = (raiz + numero / raiz) / 2

    print("La raíz cuadrada de", numero, "es", raiz)
