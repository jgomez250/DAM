# Jose Antonio Gómez Piñero - P6Ej3 - DAM - "23/10/2019"
# Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
# El programa termina escribiendo la lista de notas.

lista=[]
notas=float(input("Escriba tu nota:\n"))
while(notas<=10)and(notas>=0):
    lista.append(notas)
    notas=float(input("Escriba otra nota o para terminar escriba una nota que no esté entre 0 y 10\n"))
print("Las notas que has escrito son:",lista)
