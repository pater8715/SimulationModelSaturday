amount = float(input("¿cantidad a invertir?"))
interest = float(input("¿interes porcentual anual?"))
years = int(input("Años"))
print("capital final: " + str(round(amount * (interest / 100 + 1) ** years, 2)))