# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej8 - DAM - "24/11/2019"
# Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios
# en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.

frase=input("Escribe tu frase aqui: ")
def f(frase):
    frase=frase.replace(" ","")
    return (frase)
frase=f(frase)
print(frase)