n=int(input("Introduce la altura del triangulo (Entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")    