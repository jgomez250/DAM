# Jose Antonio Gómez Piñero - P6Ej6 - DAM - "23/10/2019"
# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista.
# Para acabar de escribir los números, escribe un número que no sea mayor que el anterior.
# El programa termina escribiendo la lista de números:

lista=[]
minNumber=int(input("Escriba un número:"))
maxNumber=int(input("Escriba un número mayor que %d:"%(minNumber)))
while(maxNumber<minNumber): #repetimos el maxNumber hasta que nos de un número menor al minNumber
    maxNumber=int(input("%d no es mayor que %d. Vuelve a probar:"%(maxNumber,minNumber)))
middleNumber=int(input("escribe un número entre %d y %d:"%(minNumber, maxNumber)))
while(middleNumber>minNumber) and (middleNumber<maxNumber): # repetimos el numero intermedio para generarlos en la lista
    lista.append(middleNumber)
    middleNumber=int(input("escribe un número entre %d y %d:"%(minNumber, maxNumber)))
#i=1 para que entre directamente en el segundo numero
#convierto el primer numero en string, si no, no podria sumarlo con los otros strings.
i=1
result=str(lista[0])#obligamos que el primer numero termine con la , y el espacio pero el segundo numero no lo lleve
for i in range(i,len(lista)):
    result=result+", "+str(lista[i]) #ejem: result=4 (4=4, "el otro numero de la lista"(6)) ahora result=4, 6 y vuelve a empezar= 4, 6(, )"el proximo numero".........
print("Los numeros situados entre %d y %d que has escrito son:"%(minNumber, maxNumber),result)
