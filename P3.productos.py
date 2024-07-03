
listaProductos = [];

def agregarProductos(coleccion):

    codigo = input("\nIngrese codigo del producto: ");
    nombre = input("Ingrese nombre del producto: ");
    cantidad = input("Ingrese cantidad del producto: ");
    precio = input("Ingrese precio del producto: ");

    coleccion.append([codigo,nombre,cantidad,precio]);

    print("\nSe agrego el producto.");

def mostrarProductos():

    contador = 1;

    if len(listaProductos) == 0:
        print("\nLa lista esta vacia.");
    else:
        for i in listaProductos:
            print(f"{contador}.- {i}");
            contador = contador + 1
        
def modificarProductos():
    mostrarProductos();

    posicion = int(input("\nIngrese el número del producto que desea modificar: "));
    codigoNuevo = input("\nIngrese codigo del producto: ");
    nombreNuevo = input("Ingrese nombre del producto: ");
    cantidadNueva = input("Ingrese cantidad del producto: ");
    precioNuevo = input("Ingrese precio del producto: ");

    listaProductos[posicion - 1] = ([codigoNuevo, nombreNuevo, cantidadNueva, precioNuevo]);
    print("\nProductos modificados correctamente.")

def guardarDatos():
    with open('Archivo_nuevo.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("     CÓDIGO   |   NOMBRE   |   CANTDAD   |   PRECIO     \n")
        for producto in listaProductos:
            archivo.write(f"{producto}\n");

while True:
    print("\n1.- Agregar");
    print("2.- Mostrar");
    print("3.- Modificar");
    print("4.- Guardar");
    
    op = int(input("\nIngrese una opcion: "));
    if op == 1:
        agregarProductos(listaProductos);
    elif op == 2:
        mostrarProductos();
    elif op == 3:
        modificarProductos();
    elif op == 4:
        guardarDatos();
    else:
        break;