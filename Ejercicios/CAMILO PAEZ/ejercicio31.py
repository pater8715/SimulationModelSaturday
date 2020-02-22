awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un numero ganador: ")))
awarded.sort()
print("Los numeros ganadores son " + str(awarded))