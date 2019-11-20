# Jose Antonio Gómez Piñero - P6Ej12 - DAM - "6/11/2019"
#Escribir un programa para jugar a adivinar un número (el usuario piensa un número y el programa lo ha de adivinar).
# El programa empieza pidiendo entre qué números está el número a adivinar y luego intenta adivinar de qué número se trata.
# El usuario va diciendo si el número que ha dicho el programa es menor, mayor o igual al que se ha buscado.

import random
listanum=[]
minimo=int(input("Valor mínimo: "))
maximo=int(input("Valor máximo: "))
while(maximo<=minimo):
    print("%d tiene que ser superior a %d"%(maximo,minimo))
    maximo=int(input("Valor máximo: "))
secreto=random.randint(minimo,maximo)
print("Piensa un número entre %d y %d a ver si lo puedo adivinar."%(minimo,maximo))
respuesta=input("Es %s? "%(secreto))#la variable secreto nos da el valor aleatorio y con el input le decimos al usuario que si es mayor o menor
while (respuesta!="igual"):
    if(respuesta=="mayor"):
        minimo=secreto+1
        secreto=random.randint(minimo,maximo)
        respuesta=str(input("Es %s? "%(secreto)))
    elif(respuesta=="menor"):
        maximo=secreto-1
        print("minimo",minimo)# hay que mirar el minimo por que da error por culpa de que supera el maximo
        print("maximo",maximo)        
        secreto=random.randint(minimo,maximo)
        respuesta=str(input("Es %s? "%(secreto)))
    if(minimo==maximo) or (maximo-minimo==1):
        print("estais haciendo trampas y no puedes contra una maquina que lee 0s y 1s.")
        respuesta=="igual"
print("Gracias por jugar!!")

"""while(numero!=secreto):
    if (numero<secreto):
        listanum.append(numero)
        numero=int(input("Demasiado pequeño! Volver a probar: "))
    elif (numero>secreto):
        listanum.append(numero)
        numero=int(input("Demasiado grande! Volver a probar: "))
listanum.append(numero)
print("Correcto! Lo has intentado %d veces."%(len(listanum)))"""
