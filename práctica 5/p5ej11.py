# Jose Antonio Gómez Piñero - P5Ej11 - DAM - "18/10/2019"
# Escribe un programa que pida un número e imprima todos sus divisores.

num=int(input("Dame un numero para imprimir sus divisores:\n"))
for i in range(1,num+1):
    if (num%i==0):
        print(i,end=" ")
"""for i in range(num+1):
    if((i!=o)and(num%i==0)):
        print(i,end=" ")"""
