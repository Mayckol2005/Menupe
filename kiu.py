flag=True
import time

contPikachuRoll=0
contOtakuRoll=0
contPulpoVenenosoRoll=0
contAnguilaEléctricaRoll=0

precio=0
totalPagar=0
decuento=0,10
totalProductos=0
PikachuRoll= 4500
OtakuRoll= 5000
PulpoVenenosoRoll= 5200
AnguilaEléctricaRoll= 4800

print("\n~~~~Hola estimado~~~~")
print(" ~~~~Bienvenido~~~~\n")
print(" ~~~Menu de Sushi~~~\n")

print("1.- Pikachu Roll--------------------$4500")
print("2.- Otaku Roll----------------------$5000")
print("3.- Pulpo Venenoso Roll-------------$5200")
print("4.- Anguila Eléctrica Roll----------$4800")
print("5.- Salir del programa\n")

while flag==True:
    opsushi=int(input("Ingrese una opcion --> "))

    if (opsushi==1):
        print("Opcion 1.")
        contPikachuRoll=contPikachuRoll+1
        totalPagar=totalPagar+PikachuRoll

    elif (opsushi==2):
        print("Opcion 2.")
        contOtakuRoll=contOtakuRoll+1
        totalPagar=totalPagar+OtakuRoll

    elif (opsushi==3):
        print("Opcion 3.")
        contPulpoVenenosoRoll=contPulpoVenenosoRoll+1
        totalPagar=totalPagar+PulpoVenenosoRoll

    elif (opsushi==4):
        print("Opcion 4.")
        contAnguilaEléctricaRoll=contAnguilaEléctricaRoll+1
        totalPagar=totalPagar+AnguilaEléctricaRoll

    elif (opsushi==5):
        print("\nSaliendo del programa...\n")
        time.sleep(1)

        totalProductos=contPikachuRoll+contAnguilaEléctricaRoll+contPulpoVenenosoRoll+contAnguilaEléctricaRoll

        flag=False

    else:
        print("\nDebe de ingresar una opcion entre 1 y 5\n")

print(f"*******************\n TOTAL PRODUCTOS:{totalProductos}\n*******************")
print(f"Pikachu Roll: {contPikachuRoll}")
print(f"Otaku Roll: {contOtakuRoll}")
print(f"Pulpo Venenoso: {contPulpoVenenosoRoll}")
print(f"Anguila Electrica: {contAnguilaEléctricaRoll}")