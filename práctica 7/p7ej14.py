# coding=utf-8
# Jose Antonio Gómez Piñero - P7Ej14 - DAM - "26/11/2019"
# Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, que recibe como
# parámetro la fecha en números y devuelve la fecha  con el nombre del mes. Comentario: no es necesario validar si la
# es correcta, damos por hecho que lo será

def ffecha(fecha):
    dia=fecha[:2]
    mes=fecha[3:5]
    año=fecha[6:]
    meses={"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio",
           "08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
    for i, j in meses.items():
        if mes==i:
            mesinput=meses.get(i)
    print(dia,"de",mesinput,"del",año)


fecha=input("Introduce una fecha en formato dd/mm/aaaa: ")
ffecha(fecha)