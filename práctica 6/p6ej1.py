# Jose Antonio Gómez Piñero - P6Ej1 - DAM - "23/10/2019"
# Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter.
# El programa termina escribiendo la lista de palabras.

lista=[]
palabra=input("Escriba una palabra:\n")
while (palabra!=""):
    lista.append (palabra)
    palabra=input("Escriba otra palabra, o pulse enter para terminar\n")
print ("Las palabras que has escrito son:",lista,end=" ")
