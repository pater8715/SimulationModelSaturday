n = int(input("Introduce un numero entero positivo mayor que 2: ")) 
i = 2
while n % i !=0:
    i +=1
if i == n:
    print(str(n) + " Es primo")
else:
    print(str(n) + " No es primo ")    