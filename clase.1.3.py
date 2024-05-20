#Declarar Variables
print()
ListaNombres = [];
ListaApellidos = [];

ListaNombres.append("Rodrigo");
ListaNombres.append("Mayckol");
ListaNombres.append("Lucho");
ListaNombres.append("Fabian");

print(ListaNombres)

nombre = input("\nIngrese un nuevo alumno: ")

ListaNombres.append(nombre)
print()
for i in ListaNombres:
    ListaNombres.pop(1)

print(ListaNombres)

print("\nCiclo For\n")
for i in range(4):
    print(f"Nombre seleccionado: {ListaNombres[i]}");

print("\nCiclo For con Lista\n")
for i in ListaNombres:
    print(f"Nombre seleccionado: {i}")

print()
