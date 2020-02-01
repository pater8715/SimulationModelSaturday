invoices = {}
collected = 0
remains = 0
more =' '
while more != 'T':
    if more == 'A':
        key = input('introduce el numero de la factura: ')
        cost= float(input('introduce el costo de la factura: '))
        invoices[key] = cost
        remains+= cost
    if more == 'P':
        key = input('introduce el numero de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('recaudado: ', collected)
    print('pendiente de cobre: ', remains)
    more = input('quieres añadir una nueva factura (A), pagarla (P) o terminarla(T)')