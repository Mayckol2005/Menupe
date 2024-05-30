'''
Actividad día Lunes
'''

#Importar Librerias
import random
import time

#Declarar Variables/Listas
listaNumeros = [1,2,3,4,5,6,7,8,9,10];
numerosSuerte = [];
listaAleatoria = [];
cont = 0

#Juego de Azar
print("\n~~~~Loteria Calfun~~~~\n");
print("Ingrese sus 5 números de la suerte.");

for i in range(5):
    num = int(input(f"Número {i+1}: "));
    numerosSuerte.append(num);

print(f"\nSus números de la suerte son: {numerosSuerte}\n");

for j in range(1,6):
    while True:
        num_aleatorio = random.randint(1,10);
        time.sleep(1);
        print(f"Se generó el siguiente número: {num_aleatorio}");
        if num_aleatorio not in listaAleatoria:
            listaAleatoria.append(num_aleatorio);
            break;

print(f"\nLos números aleatorios son: {listaAleatoria}\n");

for x in numerosSuerte:
    if x in listaAleatoria:
        cont = cont + 1;
        print(f"Usted acertó en {x}");

if cont==5:
    print("Usted se ganó la lotería. \n¡¡¡FELICIDADES!!!");
else:
    print("Usted no gano. Suerte para la próxima.\n");