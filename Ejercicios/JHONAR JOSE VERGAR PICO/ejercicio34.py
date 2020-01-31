numeros = []
for i in range(6):
    numeros.append(int(input("Introduce un número ganador: ")))
numeros.sort()
print("Los números ganadores son "+ str(numeros))