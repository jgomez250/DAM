# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej1 - DAM - "6/11/2019"
# Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes),
# los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá
# el programa por pantalla.

nombre=input("cual es su nombre?")
apellido1=input("cual es su primer apellido?")
apellido2=input("cual es su segundo apellido?")
def nombreusuario(nombre, apellido1, apellido2):
    nombrecompleto=nombre + apellido1 + apellido2 #manipulamos la cadena de string para que nos lo imprima
                                                              # todo en una unica cadena
    print (nombrecompleto)
nombreusuario(nombre, apellido1, apellido2)