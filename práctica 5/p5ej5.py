# Jose Antonio Gómez Piñero - P5Ej5 - DAM - "16/10/2019"
# Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje
alt=int(input("Cual es la altura del rectángulo?:\n"))
anch=int(input("Cual es la anchura del rectángulo?:\n"))
dib="*"
for i in range(alt):
    print(dib*anch)
