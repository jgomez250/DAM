# Jose Antonio Gómez Piñero - P5Ej10 - DAM - "18/10/2019"
# Escribe un programa que pida la altura de un rectángulo y lo dibuje
alt=int(input("Cual es la altura del rectángulo?:\n"))
dib="*"
for i in range(alt):
    if (i==alt-1):
        print(" "+dib*(i*2+1))
    else:
        print((" "*(alt-i))+dib*(i*2+1))
