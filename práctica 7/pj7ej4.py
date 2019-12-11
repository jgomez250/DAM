# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej4 - DAM - "24/11/2019"
#Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. La función debe sustituir
#todos los espacios en blanco de una frase por un asterisco, y devolver el resultado para que el programa principal
#la imprima por pantalla.

frase=input("Escribe tu frase aqui: ")
def f(frase):
    frase=frase.replace(" ","*") #reemplaza cada espacio por el asterisco
    return(frase)
frase=f(frase) #asignamos frase que tenga el valor que ha devuelto en la funcion
print(frase)