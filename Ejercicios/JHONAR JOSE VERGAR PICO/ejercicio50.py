compra= {}
more = 'si'
while more == 'si':
    item = input('digite un articulo')
    precio = float(input('digite el precio de '+ item + ': '))
    compra[item]= precio
    more = input('quieres añadir mas articulos a la lista (si/no)')
costo = 0
print('lista de la compra')
for item, precio in compra.items():
    print(item, '\t', precio)
    costo += precio
print ('costo total: ', costo)