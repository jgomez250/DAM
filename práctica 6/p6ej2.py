# Jose Antonio Gómez Piñero - P6Ej2 - DAM - "23/10/2019"
# Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”.
# El programa termina escribiendo la lista de números.
lista=[]
num=int(input("Escribe un número:\n"))
while(num!="Salir"):
    num=int(num)
    lista.append (num)
    num=input("Escribe un número o para terminar escriba 'Salir'\n")
print ("Los números que has escrito son:",lista,end=" ")
