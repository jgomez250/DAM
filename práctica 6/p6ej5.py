# Jose Antonio Gómez Piñero - P6Ej5 - DAM - "23/10/2019"
# Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista.
# Para acabar de escribir los números, escribe un número que no sea mayor que el anterior.
# El programa termina escribiendo la lista de números:

lista=[]
previousnumber=int(input("Escriba un número:"))
lista.append(previousnumber)
nextnumber=int(input("Escriba un número mayor que %d o menor para salir:"%(previousnumber)))
while(previousnumber<nextnumber):
    lista.append(nextnumber)
    previousnumber=nextnumber
    nextnumber=int(input("Escriba un número mayor que %d o menor para salir:"%(previousnumber)))
result=str(lista[0])
for i in range(1,len(lista)):
    result=result+", "+str(lista[i])
print(result)
