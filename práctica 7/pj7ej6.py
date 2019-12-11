# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej6 - DAM - "24/11/2019"
# Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una función que comprobará
# si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.

nombre=input("Cual es tu nombre?: ")
caracter=input("Escriba un caracter y comprobaremos si esta en él ")
def f(nombre,caracter):
    if caracter in nombre: #comprobamos que el caracter este dentro de nombre
        return True
    else:
        return False
f(nombre,caracter)
print("El caracter '%s' que buscas en '%s' es: %s"%(caracter,nombre,f(nombre,caracter)))#podemos añadir funciones en %s