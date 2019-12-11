# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej7 - DAM - "24/11/2019"
# Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El procedimiento contará el
# número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

frase=input("Escribe tu frase aqui: ")
def f(frase):
    i=0 #i sera el valor incrementado tanto para vocales como para letras
    vocal=0 #vocal es el valor que incrementa cuando hay una vocal
    while i<len(frase):
        if frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u":
            vocal+=1
            i+=1
        else: #el else esta para que aun que no sea una vocal no entre en un bucle infinito
            i+=1
    print(vocal)

f(frase)