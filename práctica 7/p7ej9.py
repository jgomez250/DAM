# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej9 - DAM - "24/11/2019"
# Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman o no.
# Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que
# riman un poco y si no, que no riman.

word1=input("Dime una palabra: ")
word2=input("Dime otra palabra: ")
def f(word1,word2):
    if word1[-3:]==word2[-3:]:
        print("Las palabras %s y %s riman."%(word1, word2))
    elif word1[-2:]==word2[-2:]:
        print("Las palabras %s y %s riman un poco."%(word1, word2))
    else:
        print("Las palabras %s y %s no riman." % (word1, word2))
f(word1,word2)