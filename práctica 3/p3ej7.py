# Jose Antonio Gómez Piñero - P3Ej7 - DAM - 9-10-2019
# Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha introducida es válida.

dia=int(input("introduce el dia"))
if (dia>31)or(dia<1) :
    print("La fecha introducida no es válida.")
else:
    mes=int(input("introduce el mes(el número del mes)"))
    if mes<1 or mes>12:
        print("La fecha introducida no es válida.")
        if mes==2 and dia>28 or dia<1:
            print("La fecha introducida no es válida.")
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>31 or dia<1:
                print("La fecha introducida no es válida.")
        if mes==4 or mes==6 or mes==9 or mes==11 and dia>30 or dia<1:
             print("La fecha introducida no es válida.")
    else:
        año=int(input("introduce el año"))
        if (año<1)or(año>2020):
            print("La fecha introducida no es válida.")
        else:
            print(dia,"/",mes,"/",año)
