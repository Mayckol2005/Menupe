flag = True

s = 0
afp = 0.1
fonasa = 0.07
hora_extra = 0
hora = 1.5

while flag==True:

    nom=input("\nHola usuario, ingrese su nombre: ")
    try:
        sueldo_bruto = int(input("Ingrese su Sueldo Bruto: "))
        hora_extra = int(input("Ingrese sus Horas Extras: "))
    except ValueError:
        print("\nIngrese un valor valido, por favor...")
    else:
        
        s = hora_extra*hora
        monto_extra=(sueldo_bruto/180)*s
        sueldo_bruto_total = monto_extra+sueldo_bruto
        total_descuento = sueldo_bruto*(afp+fonasa)
        descuentoAfp = sueldo_bruto*afp
        descuentoFonasa = sueldo_bruto*fonasa
        sueldo_liquido = sueldo_bruto-total_descuento

        flag=False

print("\nLiquidación de Sueldo\n-----------------")

print(f"Sueldo Bruto: ${sueldo_bruto:.0f}")
print(f"Horas Extras: {hora_extra:.0f}")
print(f"Monto Horas Extras: ${monto_extra:.0f}")
print(f"Sueldo Bruto Total: ${sueldo_bruto_total:.0f}")
print(f"Descuento AFP (10%): ${descuentoAfp:.0f} ")
print(f"Descuento FONASA (7%): ${descuentoFonasa:.0f}")
print(f"Total Descuentos: ${total_descuento:.0f}")
print(f"Sueldo Líquido: ${sueldo_liquido:.0f}\n")