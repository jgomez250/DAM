# Jose Antonio Gómez Piñero - P3Ej6 - DAM - 9-10-2019
# Pida al usuario el precio de un producto y el nombre del producto
# y muestre el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.

nombre=input("Que producto deseas vender?\n")
precio=float(input("El precio del producto es?\n"))
IVA=precio*1.21
print("Tu",nombre,"vale",precio,"euros y con el 21 % de IVA se queda en",IVA,"euros en total")
