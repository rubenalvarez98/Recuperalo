distancia_metros = float(input("Ingrese la distancia en metros: "))

# Convertir a kilómetros, centímetros y milímetros
distancia_kilometros = distancia_metros / 1000
distancia_centimetros = distancia_metros * 100
distancia_milimetros = distancia_metros * 1000

print("Distancia: {} kilómetros, {} centímetros, {} milímetros".format(distancia_kilometros, distancia_centimetros, distancia_milimetros))
