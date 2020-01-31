letras = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales: 
    tiempo = 0
    for palabras in letras: 
        if palabras == vocal:
            tiempo += 1
    print("La vocal " + vocal + " aparece " + str(tiempo) + " veces")