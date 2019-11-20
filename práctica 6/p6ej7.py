# Jose Antonio Gómez Piñero - P6Ej7 - DAM - "30/10/2019"
# Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial.
# El programa termina escribiendo la lista de números.

lista=[]
limitNumber=int(input("Escriba un número limite:\n"))
maxNumber=int(input("Escriba un valor:\n"))
lista.append(maxNumber)
aux_maxNumber=maxNumber #agregamos una tercera variante para que nos sume el total de los numeros que añadiremos(maxNumber) en la lista 
while(maxNumber<=limitNumber) and (aux_maxNumber<=limitNumber):
    maxNumber=int(input("escribe otro valor:\n"))
    lista.append(maxNumber)
    aux_maxNumber+=maxNumber
#i=1 para que entre directamente en el segundo numero
#convierto el primer numero en string, si no, no podria sumarlo con los otros strings.
i=1
result=str(lista[0])#obligamos que el primer numero termine con la , y el espacio pero el segundo numero no lo lleve
for i in range(i,len(lista)):
    result=result+", "+str(lista[i]) #ejem: result=4 (4=4, "el otro numero de la lista"(6)) ahora result=4, 6 y vuelve a empezar= 4, 6(, )"el proximo numero".........
# print("el límite a superar es %d. La lista creada es",result,"ya que la suma de estos números es:"%(limitNumber),aux_maxNumber) (fallo por mesclar % y variables)
print("El límite a superar es %d. La lista creada es %s ya que la suma de estos números es: %d"%(limitNumber, result, aux_maxNumber))
