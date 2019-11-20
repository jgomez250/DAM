# Jose Antonio Gómez Piñero - P6Ej10 - DAM - "6/11/2019"
# Escribe un programa que te pida los nombres y notas de alumnos. Si escribes una nota fuera del intervalo de 0 a 10, el programa
# entenderá que no quieres introducir más notas de este alumno. Si no escribes el nombre, el programa entenderá que no quieres
# introducir más alumnos. Nota: La lista en la que se guardan los nombres y notas tiene esta estructura
# [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]

mainlist=[]
aux=[]
name=input("Dame un nombre: ")
while (name!=""):
    aux.append(name)
    qualification=float(input("Escribe una nota: "))
    while (qualification<=10) and (qualification>=0):
        aux.append(qualification)
        qualification=float(input("Escribe otra nota: "))
    mainlist.append(aux)
    aux=[]
    name=input("Dame un nombre: ")
print("\nLas notas de los alumnos son: ")
for i in range(len(mainlist)):
    print("%s:"%(mainlist[i][0]),end=" ")
    print("%s"%(mainlist[i][1]),end=" ")#imprimimos la primera nota para que no entre con el guion
    for j in range(2,len(mainlist[i])):#que entre en el segundo numero por que ya imprimimos el nombre y la primera nota
        print("- %s"%(mainlist[i][j]),end=" ")
    print("") #nos da un salto de linea entre la nota final y el nombre para separarlos
