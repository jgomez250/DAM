# Jose Antonio Gómez Piñero - P5Ej4 - DAM - "16/10/2019"
# Escribe un programa que pida un número y calcule su factorial.

num1=int(input("Dame un número factorial:\n"))
fact=1
for i in range(1,num1+1):
    fact=i*fact
print("El valor del numero factorial es:",fact)
