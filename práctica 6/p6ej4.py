# Jose Antonio Gómez Piñero - P6Ej4 - DAM - "23/10/2019"
# Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero.
# El programa termina escribiendo los dos números tal y como se pide

lista=[]
num1=int(input("Escriba un número:"))
lista.append(num1)
num2=int(input("Escriba un número mayor que %d:"%(num1)))
while(num1>=num2):
    print(num2,"no es mayor que",num1)
    num2=int(input("Vuelve a introducir un número:"))
lista.append(num2)
print("Los números que has escrito son",lista[0],"y",lista[1])
