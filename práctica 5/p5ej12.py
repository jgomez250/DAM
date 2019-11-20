# Jose Antonio Gómez Piñero - P5Ej12 - DAM - "18/10/2019"
# Escribe un programa que pida un número y escriba si primo o no

num=int(input("Dame un numero y te diré si es o no primo:\n"))
resto=1
for i in range(1,num):
    if (num%i==0) and (i!=1):
        resto=0
if (resto==1):
    print(num,"Es primo")
else:
    print(num,"No es primo")
