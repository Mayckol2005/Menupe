#w3schoolas.com

#Declarar

print()
rango = range(5);
texto = "Hola Mundo";
listaDeportes = ["Futbol","Rugby","Basquetball","HandBall"];
matrizNumerica = [[1,2,3],
                  [4,5,6],
                  [7,8,9]];

#For que recorre e imprime un rango de valores númericos [0,1,2,3,4]
print("1) For utilizando Range(5)")
for elemento in rango:
    print(elemento,end=" - ");

#For que recorre e imprime un rango de caracteres [Hola Mundo]
print("\n")
print("2) For utilizando Texto")
for elemento in texto:
    print(elemento,end=" - ");

#For que recorre e imprime un rango de valores de una lista [Deportes]
print("\n")
print("3) For utilizando Listas")
for elemento in listaDeportes:
    print(elemento,end=" - ");

#For que recorre e imprime un rango de valores de una Matriz [Números]
print("\n")
print("4) For utilizando Matriz")
for elemento in matrizNumerica:
    print(elemento,end=" - ");
print("\n")

for elemento in matrizNumerica:
    for elemento1 in elemento:
        print(elemento1,end=" - ")
print("\n")


    