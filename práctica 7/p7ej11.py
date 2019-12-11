# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej11 - DAM - "26/11/2019"
# Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. Ésta debe devolver si es
# palíndroma o no , y el programa principal escribirá el resultado por pantalla

dato=input("Dime algo: ")
def f(dato):
    dat2=""
    for j in range(len(dato)-1,-1,-1):
        dat2+=dato[j]
    aux1=dat2.replace(" ","")
    aux2=dato.replace(" ","")
    if aux1==aux2:
        return print("%s es capicúa o palíndroma"%(dato))
    else:
        return print("%s no es capicúa o palíndroma"%(dato))
dato=f(dato)