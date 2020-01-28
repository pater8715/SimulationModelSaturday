amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interes porcentual anual? "))
years = int(input("¿Años?"))
print("Capital final: " + str(round(amount * (interest / 100 + 1) ** years, 2)))