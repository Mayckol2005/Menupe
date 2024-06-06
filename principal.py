import funciones as funcion
import time

try:
    n1 = int(input("\nIngrese un número: "))
    n2 = int(input("Ingrese otro número: "))
except:
    print("Ingresar número valido...")
else:

    print()

    while True:
        print("~~~Menú Calculadora Duoc~~~\n");
        print("1.- Sumar.");
        print("2.- Restar.");
        print("3.- Multiplicar.");
        print("4.- Dividir.");
        print("5.- Salir.\n");
        try:
            op = int(input("Ingrese la opción: "))
        except:
            print("Error... Ingresar número del 1 - 5")
        else:
            if (op == 1):
                funcion.suma(n1,n2);
                print()

            elif (op == 2):
                funcion.resta(n1,n2);
                print()

            elif (op == 3):
                funcion.multi(n1,n2);
                print()
            
            elif (op == 4):
                funcion.divi(n1,n2);
                print()

            elif (op == 5):
                print("Saliendo del programa...")
                print()

                time.sleep(2)
                break;
            else:
                print("La opción no es valida...")      