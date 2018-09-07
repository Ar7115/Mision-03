#Autor: Luis Armando Miranda Alcocer
# Calcula el precio de 3 tipos de boletos.

def calcularPago (asientosA, asientosB, asientosC):
    pagoA = asientosA * 925
    pagoB = asientosB * 775
    pagoC = asientosC * 360
    totalPago = pagoA + pagoB + pagoC
    return totalPago #Regresar totalPago de acuerdo a los datos previamente calculados y leídos.

def main():
    asientosA = int(input("Número de boletos de Clase A: ")) # Leer datos
    asientosB = int(input("Número de boletos de Clase B: "))
    asientosC = int(input("Número de boletos de Clase C: "))
    totalPago= calcularPago(asientosA, asientosB, asientosC) #Llamar a la función calcularPago
    print ("El costo total es: $%.2f" %(totalPago))
# Llamar a la función principal para que funcione el programa
main()