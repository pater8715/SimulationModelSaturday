num = int(input("introduce un número entero: "))
i = 2
while num % i != 0:
    i += 1
if i == num:
    print(str(num) + " es primo")
else:
    print(str(num) + " no es primo")