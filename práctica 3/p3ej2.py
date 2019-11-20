# Jose Antonio Gómez Piñero - P3Ej2 - DAM - 9-10-2019
# Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado en horas y que calcule a qué velocidad media había realizado el recorrido.

distancia=int(input("Cual es la distancia recorrida(km) con el coche?\n"))
tiempo=int(input("Que tiempo has tardado?(h)\n"))
vel_media=distancia/tiempo
print("la velocidad media es:\n",vel_media,"km/h")
