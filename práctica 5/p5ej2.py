# Jose Antonio Gómez Piñero - P5Ej3 - DAM - "15/10/2019"
# Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.

num1=int(input("Cual es su numero?:\n"))
num2=int(input("Dame un numero mayor que"))
if num2>num1:
    for i in range(num1,num2+1):
        print(num1)
else:
    print(num2,"es más pequeño que",num1,". No se realizará la comparación")
