amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interes porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100
    print ("Capital tras " + str(i+1) + " Años: " + str(round(amount, 2)))