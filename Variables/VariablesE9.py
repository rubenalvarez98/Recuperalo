valor_unitario = float(input("Ingrese el valor unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))

subtotal = valor_unitario * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print("Subtotal: $", subtotal)
print("IVA (16%): $", iva)
print("Total a pagar: $", total)
