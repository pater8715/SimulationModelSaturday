income = float(input("¿cual es tu renta anual? "))
if income < 10000:
    tax = 5
elif income < 20000:
        tax = 15
elif income < 35000:
        tax = 20
elif income < 60000:
        tax = 30
else:
        tax = 45
print("tu tipo impositivo es " + str(tax) + "%") 