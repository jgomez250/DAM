# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej12 - DAM - "26/11/2019"
# Escribir un programa que lea una frase, y pase ésta como parámetro a una función que debe contar el número de
# palabras que contiene. Debe imprimir el programa principal el resultado. Asumir que cada palabra está separada por un
# solo blanco

"""frase=input("Escribe una frase: ") -------------------------A-----------------------
def f(frase):
    frasenum=frase.count(" ")
    frasenum+=1
    return frasenum
frasenum=f(frase)
print("%s contiene %d palabras."%(frase,frasenum))"""

frase=input("Escribe una frase: ")   #-------------------------B-----------------------
def f(frase):
    for i in frase:
        palabras=frase.split()
        frasenum=len(palabras)
    return frasenum
frasenum=f(frase)
print("%s contiene %d palabras."%(frase,frasenum))