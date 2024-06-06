import funciones as funcion
import time

print("\n~~~ Ferreteria DUOC ~~~\n")
print("      ~~ Menú ~~\n")

while True:
    print("1.- Agregar Producto.")
    print("2.- Mostrar Producto.")
    print("3.- Buscar Producto.")
    print("4.- Eliminar Producto.")
    print("5.- Salir.\n")

    op = int(input("¿Que desea hacer? (Ingrese una opcion) -->"));

    if (op == 1):
        funcion.agregarProductos();
        print();

    elif (op == 2):
        funcion.mostrarProductos();
        print();

    elif (op == 3):
        funcion.buscarProductos();

    elif (op == 4):
        funcion.eliminarProductos();

    elif (op == 5):
        print("Saliendo del programa...")
        time.sleep(1);
        break
    else:
        print("Ingrese una opcion valida...")
