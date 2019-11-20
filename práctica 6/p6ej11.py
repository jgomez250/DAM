# Jose Antonio Gómez Piñero - P6Ej11 - DAM - "6/11/2019"
# Escribir un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario lo ha de adivinar). El programa empieza pidiendo entre qué
# números está el número a adivinar, se "inventa" un número al azar y luego el usuario va probando valores. El programa va decidiendo si son demasiado grandes o pequeños.

import random
listanum=[]
minimo=int(input("Valor mínimo: "))
maximo=int(input("Valor máximo: "))
secreto=random.randint(minimo,maximo)
print("A ver si adivinas un número entero entre %d y %d."%(minimo,maximo))
numero=int(input("Escribe un número:"))
while(numero!=secreto):
    if (numero<secreto):
        listanum.append(numero)
        numero=int(input("Demasiado pequeño! Volver a probar: "))
    elif (numero>secreto):
        listanum.append(numero)
        numero=int(input("Demasiado grande! Volver a probar: "))
listanum.append(numero)
print("Correcto! Lo has intentado %d veces."%(len(listanum)))
