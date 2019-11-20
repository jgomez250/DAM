# Jose Antonio Gómez Piñero - P5Ej9 - DAM - "18/10/2019"
# Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje
alt=int(input("Cual es la altura del rectángulo?:\n"))
anch=int(input("Cual es la anchura del rectángulo?:\n"))
dib="*"
for i in range(alt):
    if (i<=0)or(i==alt-1):
        print(dib*anch)
    elif (i<0)or(i<alt):
        print(dib+(" "*(anch-2))+dib)
