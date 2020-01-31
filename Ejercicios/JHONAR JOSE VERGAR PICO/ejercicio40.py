numeros = [50, 75, 46, 22, 80, 65, 8]
min = max = numeros[0]
for num in numeros:
    if num < min:
        min = num
    elif num > max:
        max = num 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))