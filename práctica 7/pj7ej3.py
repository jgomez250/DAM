# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej3 - DAM - "24/11/2019"
# Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con
# un carácter en cada línea.

frase=input("Escribe tu frase aqui: ") #pasamos por parametro frase en el procedimiento
def f(frase):
    for caracter in frase: # el valor caracter coge cada posicion del string frase "el caracter" y lo va imprimiendo
        print(caracter)

f(frase)