amount = float(input("¿cantidad a invertir? "))
interest = float(input("¿interes porcentual anual? "))
years = int(input("¿años?"))
for i in range(years):
    amount *= 1 + interest / 100
    print("capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
    