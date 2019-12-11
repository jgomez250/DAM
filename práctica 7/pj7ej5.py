# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej5 - DAM - "24/11/2019"
# Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función que se
# encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase
# modificada, y el programa principal la imprimirá:

frase=input("Escribe tu frase aqui: ")
vocal=input("Escribe tu vocal: ")
def f(frase):
    frase=frase.replace("a",vocal) #reemplaza cada vocal con la vocal introducida por el usuario
    frase=frase.replace("e", vocal)
    frase=frase.replace("i", vocal)
    frase=frase.replace("o", vocal)
    frase=frase.replace("u", vocal)
    return(frase)
frase=f(frase) #asignamos frase que tenga el valor que ha devuelto en la funcion
print(frase)