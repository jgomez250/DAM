# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej10 - DAM - "24/11/2019"
# Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función, y ésta te diga
# si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:

dato=input("Dime algo: ")
def f(dato):
    dat2=""
    for j in range(len(dato)-1,-1,-1):
        dat2+=dato[j]
    if dat2==dato:
        return print("%s es capicúa o palíndroma"%(dato))
    else:
        return print("%s no es capicúa o palíndroma"%(dato))
dato=f(dato)