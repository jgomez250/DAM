# Jose Antonio Gómez Piñero - P5Ej8 - DAM - "16/10/2019"
# Escribe un programa que pida la anchura de un triángulo y lo dibuje
anch=int(input("Cual es la anchura del triángulo?:\n"))
dib="*"
"""for i in range(1,anch+1):
    print(dib*i)
for i in range(anch-1,0,-1):
    print(dib*i)"""

for i in range (anch*2):
    if(i<=anch):
        print(dib*i)
    elif(i>anch):
        print(dib*(-i+(anch*2)))
