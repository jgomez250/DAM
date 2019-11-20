# Jose Antonio Gómez Piñero - P5Ej7 - DAM - "16/10/2019"
# Escribe un programa que pida la altura de un triángulo y lo dibuje

alt=int(input("Cual es la altura del triángulo?:"))
dib="*"
for i in range(alt,0,-1):
    print(dib*i)
