cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

# Calcular el cuadrado de los catetos
cateto1_cuadrado = cateto1 ** 2
cateto2_cuadrado = cateto2 ** 2

# Calcular la suma de los cuadrados de los catetos
suma_cuadrados = cateto1_cuadrado + cateto2_cuadrado

# Calcular la hipotenusa tomando la raíz cuadrada de la suma de los cuadrados
hipotenusa = suma_cuadrados ** 0.5

print("La hipotenusa es:", hipotenusa)

