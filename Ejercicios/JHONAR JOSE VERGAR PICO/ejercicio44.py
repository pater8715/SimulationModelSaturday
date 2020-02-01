moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
money = input("Introduce una divisa: ")
print(moneda.get(money.title(), "La divisa no está."))