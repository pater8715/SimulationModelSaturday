frase = input("introduce una frase: ")
letra = input("introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("la letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))