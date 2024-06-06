def suma(num1,num2):
    suma = (num1 + num2)
    print(f"Suma: {suma}");

def resta(num1,num2):
    resta = (num1 - num2);
    print(f"Resta: {resta}");

def multi(num1,num2):
    multi = (num1 * num2);
    print(f"Multiplicacion: {multi}");

def divi(num1,num2):
    divi = (num1 / num2);
    print(f"Division: {divi}");

#Crear un sistema de Administración de Productos de una Ferreteria
#Funcion para agregar productos
#Funcion para mostrar productos
#Funcion para buscar productos
#Funcion para eliminar productos

listaProductos = ["Martillo","Hacha","Pala","Cemento"];

def agregarProductos():
    producto = input("Ingrese el nuevo producto --> ");
    listaProductos.append(producto)
    print("El producto se ingresó correctamente.");

def mostrarProductos():
    print(f"La lista de productos es: {listaProductos}");

def buscarProductos(producto):
    if producto in listaProductos:
        print("El producto SI esta en la lista.");
        return True;
    else:
        print("El producto NO esta en la lista.")
        return False;
        

def eliminarProductos():
    print();