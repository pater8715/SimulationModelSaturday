diccionario ={}
palabras = input("introduce la lista de palabras y traducciones en formato palabra:traduccion separadas por coma: ")
for i in palabras.split(','):
    key, value = i.split(':')
    diccionario[key] = value
frase = input('introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')