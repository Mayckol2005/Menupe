#Ejemplos
""""
num=int(input("Ingrese un numero: "))

listaTabla = []

for i in range(1,11):

    listaTabla.append(i*num)

print(listaTabla)
"""""
"""""
listaTabla1 = []
print("\n\n")

flag = True

while flag==True:
    num1=int(input("Ingrese un numero: "))
    listaTabla1.append(num1)
    if num1==0:

        flag=False

listaTabla1.sort()
print(listaTabla1)
"""""

"""""
print("\n\n")

listaTabla2 = []

flag = True
resultado = 0

for i in range(10):

    num2 = int(input("Ingrese un numero: "))

    listaTabla2.append(num2)
    resultado=resultado+num2

print(listaTabla2)
print(resultado)
resultado1=resultado/10
print(resultado1)
"""""

print("\n\n")

listaNombres = []

for i in range(3):
    nom=input("Ingrese un nombre: ")

    listaNombres.append(nom)

print("\n",listaNombres,"\n")

print(len(listaNombres[0]))
print(len(listaNombres[1]))
print(len(listaNombres[2]))

