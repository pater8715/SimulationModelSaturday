numeros = input("Introduce una muestra de números separados por comas: ")
numeros = numeros.split(',')
num = len(numeros)
for i in range(num):
    numeros[i] = int(numeros[i])
numeros = tuple(numeros)
suma = 0
sumas = 0
for i in numeros:
    suma += i
    sumas += i**2
media = suma/num
dest = (sumas/num-media**2)**(1/2)
print('La media es', media, ', y la desviación típica es', dest)