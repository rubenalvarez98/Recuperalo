total_notas = int(input("Ingrese la cantidad total de notas: "))

suma_notas = 0.0

# Solicitar las notas individuales y sumarlas
for i in range(total_notas):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    suma_notas += nota

# Calcular el promedio
promedio = suma_notas / total_notas

# Mostrar el resultado
if promedio >= 3.0:
    print("Aprobó")
else:
    print("No aprobó")
