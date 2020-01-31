age = int(input("¿cual es tu edad? "))
income = float(input("¿cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("tienes que cotizar")
else:
    print("no tienes que cotizar")