# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej13 - DAM - "26/11/2019"
# Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, por tanto,
# habrán dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra
# (con while). Ambas funciones devolverá true (si es es primo) o false (si no es primo). El programa principal informará
# del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra.
# Comentario: aprovecha el código que tienes ya creado

import time

def ffor(numero):
    resto=1
    for i in range(numero):
        if i!=0 and i!=1 and numero%i==0:
            resto=0
    if resto==0:
        return False
    else:
        return True


def fwhile(numero):
    resto=1
    aux=1
    while (resto != 0):
        aux+=1
        resto=numero%aux
    if aux==numero:
        return True
    else:
        return False
#------------------------------------------------------------

numero=int(input("Dame un número: "))
start=time.time()
print("el resultado de si es o no primo el numero %d es: %s"% (numero,ffor(numero)))
res=time.time()-start
print("\nEl for tarda: %.10f segundos."% res)
start=time.time()
res=time.time()-start
print("El while tarda: %.10f segundos."% res)