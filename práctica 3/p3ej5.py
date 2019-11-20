# Jose Antonio Gómez Piñero - P3Ej5 - DAM - 9-10-2019
# Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario
#introduce un número de más de tres cifras debe un informar con un mensaje de error como este “ ERROR: El número 1005 tiene más de tres cifras”.
num1=int(input("Pida un número el cual no exceda de 999:\n"))
if (num1>=1000):
    print("ERROR: El número",num1,"tiene más de tres cifras")
else:
    print(num1)
