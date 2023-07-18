nombre=(input("Digite su nombre: "))
edad=int(input("Digite su edad: "))
if edad <=0 or edad>=100:
    print('Ingrese un dato correcto')
elif edad >=18:
    print(nombre,'usted es mayor de edad')
else :
    print(nombre,'usted es menor de edad')
print('fin del programa')