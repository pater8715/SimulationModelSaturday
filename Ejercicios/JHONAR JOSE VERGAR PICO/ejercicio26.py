num = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")
    