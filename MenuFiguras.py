"""
 for i in range(altura):
                print("*")
                for j in range(base):
                    print("*"*1)
                print()
"""


flag=True

#Menu de opciones

print("\n~~~~~Programa informatico~~~~~\n")

while flag:

    figura1=input("~~~Hola usuario, que figura desea ingresar: ")
    print('')
    if figura1=="triangulo":

        base=int(input("Porfavor ingrese la base: "))
        altura=int(input("Porfavor ingrese un lado: "))
        altura1=int(input("Porfavor ingrese otro lado: "))

        print('')
        print("¿Que desea saber?\n")
        print("1.- Area")
        print("2.- Perimetro")
        print("3.- Dibujo\n")
        op=int(input("***Eliga una opcion ---> "))

        if op==1:
            
            print("Elegiste la opcion 1\n\nArea\n")
            area=base*altura
            print(f"El area del triangulo es de {area}\n")

        elif op==2:

            print("Elegiste la opcion 2\n Perimetro")
            perimetro=base+altura+altura1
            print(f"El perimetro del triangulo es {perimetro}")

        elif op==3:

           print("Elegiste la opcion 3\n Dibujo")

    elif figura1=="cuadrado":

        ladoCua=int(input("Ingrese un lado: "))

        print('')
        print("¿Que desea saber?\n")
        print("1.- Area")
        print("2.- Perimetro")
        print("3.- Dibujo\n")
        op=int(input("***Eliga una opcion ---> "))
        print("")
        if op==1:
            
            print("Elegiste la opcion 1\n\nArea\n")
            area=ladoCua*ladoCua
            print(f"El area del cuadrado es de {area}\n")

        elif op==2:

            print("Elegiste la opcion 2\nPerimetro\n")
            perimetro=ladoCua*4
            print(f"El perimetro del cuadrado es {perimetro}\n")

        elif op==3:

           print("Elegiste la opcion 3\nDibujo\n")

           for i in range(ladoCua):
                for j in range(ladoCua):
                   print(" * ", end="")
                print("")
                print("\n")

    elif figura1=="rectangulo":

        ladoRec=int(input("Ingrese la altura: "))
        ladoRec1=int(input("Ingrese la base: "))

        print('')
        print("¿Que desea saber?\n")
        print("1.- Area")
        print("2.- Perimetro")
        print("3.- Dibujo\n")
        op=int(input("***Eliga una opcion ---> "))
        print("")
        if op==1:
            
            print("Elegiste la opcion 1\n\nArea\n")
            area=ladoRec*ladoRec1
            print(f"El area del rectangulo es de {area}\n")

        elif op==2:

            print("Elegiste la opcion 2\nPerimetro\n")
            perimetro=ladoRec*2+ladoRec1*2
            print(f"El perimetro del rectangulo es {perimetro}\n")

        elif op==3:

           print("Elegiste la opcion 3\nDibujo\n")

           for i in range(ladoRec):
                for j in range(ladoRec1):
                   print(" * ", end="")
                print("")