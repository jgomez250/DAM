# Jose Antonio Gómez Piñero - P6Ej9 - DAM - "5/11/2019"
# Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar debe pulsar “S” cuando te pida el nombre.
# El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono
# tiene esta estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.

mainlist=[]
name=input("Dame un nombre: ")
while (name!="S"):
    telephone=int(input("Dame el teléfono: "))
    mainlist.append([name, telephone])#agregamos sublista con los corchetes
    name=input("Dame un nombre o escriba 'S' para salir: ")
print("\nLos nombres y teléfonos de la agenda son: ") #ponemos el print fuera, si no lo repite varias veces
for i in range(len(mainlist)): #aqui repetimos los valores (name y telephone)
    print("%s: %d"%(mainlist[i][0], mainlist[i][1]))# el indice 0 sera el nombre y el 1 sera el telefono
