import time 

#Declarar variables

flag=True

#Menu de opciones

while flag:
    print("\n~~~~~Menu de opciones~~~~\n")
    print("1.- Sumar dos numeros.")
    print("2.- Conocer número PAR.")
    print("3.- Dibujar un cuadrado.")
    print("4.- Salir del programa.\n")
    try:
        op=int(input("***Ingrese una opción --> "))
    except ValueError:
        print("\nError al ingresar opción, elija una opción entre 1 y 4. Vuelva a intentarlo")
    else:
        if op==1:
            print("Elegiste la opción 1.\n")
            print("Sumar dos números.\n")
            try:
                num1=int(input("Ingrese un número: "))
                num2=int(input("Ingrese un número: "))
                print(f"\nEl resultado de {num1} + {num2} = {num1+num2}")
            except:
                print("\nError, debe de ingresar un número. Vuelva a intentarlo")
        elif op==2:
            print("Elegiste la opción 2.\n")
            print("Conocer número PAR.\n")
            try:
                num=int(input("Ingrese un número: "))
                if num%2==0:
                        print(f"\n{num}, es par")
            except:
                print("\nError, debe de ingresar un número. Vuelva a intentarlo")
        elif op==3:
            print("Elegiste la opción 3.\n")
            print("3.- Dibujar un cuadrado.\n")
            try:
                lado1=int(input("Ingrese una medida: "))
                print('')
            except:
                print("\nError, debe de ingresar un número. Vuelva a intentarlo")
            else:
                for i in range(lado1):
                    for j in range(lado1):
                        print("*",end="")
                    print("")   
        elif op==4:
            print("\nElegiste la opción 4.\n")
            print("Saliendo del programa...")
            time.sleep(2)
            flag=False
        elif op > 4 or op < 0:
            print("Error... Debe de ingresar una opcion valida.")