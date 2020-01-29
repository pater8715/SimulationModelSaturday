inversion = float(input("Digite la cantidad a invertir: "))
interes = float(input("Porcentaje de interes: "))
años = int(input("Digite el numero de años: "))
for i in range(años):
    inversion *= 1 + interes / 100
    print("Capital tras "+ str(i+1) + " años: " + str(round(inversion, 2)))