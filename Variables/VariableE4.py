print("‐-----4.Edad------")

from datetime import date

anio_actual = date.today().year

anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

edad = anio_actual - anio_nacimiento

print("Tu edad es:", edad, "años")
