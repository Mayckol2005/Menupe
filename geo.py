altura = int(input("Ingresa la altura del triángulo: "))

for i in range(1, altura + 1):
    
   
    print("*" * i)





altura = int(input("Ingresa la altura del triángulo: "))

# Itera sobre cada fila del triángulo
for i in range(altura):
    
   
# Imprime espacios en blanco para alinear los asteriscos
    
   
    for j in range(altura - i - 1):
        
       
        print(" ", end="")

    for k in range(2 * i + 1):
        
       
        print("*", end="")
        
    print()