tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))

# Calcular horas, minutos y segundos
horas = tiempo_segundos // 3600
minutos = (tiempo_segundos % 3600) // 60
segundos = (tiempo_segundos % 3600) % 60

print("Tiempo: {} hora(s), {} minuto(s), {} segundo(s)".format(horas, minutos, segundos))
