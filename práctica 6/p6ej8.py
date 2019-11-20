# Jose Antonio Gómez Piñero - P6Ej8 - DAM - "30/10/2019"
# Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial.
# El programa termina escribiendo la lista de números.

lista=[]
limitNumber=int(input("Escriba un número limite:\n"))
maxNumber=int(input("Escriba un valor:\n"))
lista.append(maxNumber)
aux_maxNumber=maxNumber #agregamos una tercera variante para que nos sume el total de los numeros que añadiremos(maxNumber) en la lista 
while(aux_maxNumber!=limitNumber):
    if(aux_maxNumber<limitNumber):
        maxNumber=int(input("escribe otro valor:\n"))
        aux_maxNumber+=maxNumber
        lista.append(maxNumber)
    elif(aux_maxNumber>limitNumber):
        lista.remove(maxNumber)
        aux_maxNumber-=maxNumber
        maxNumber=int(input("%d es demasiado grande.Escribe otro valor: "%(maxNumber)))
        aux_maxNumber+=maxNumber
        lista.append(maxNumber)
#convierto el primer numero en string, si no, no podria sumarlo con los otros strings.
result=str(lista[0])#obligamos que el primer numero termine con la , y el espacio pero el segundo numero no lo lleve
for i in range(1,len(lista)):
    result=result+", "+str(lista[i]) #ejem: result=4 (4=4, "el otro numero de la lista"(6)) ahora result=4, 6 y vuelve a empezar= 4, 6(, )"el proximo numero".........
print("El límite a alcanzar es %d. La lista creada es %s es: %d"%(limitNumber, result, limitNumber))
