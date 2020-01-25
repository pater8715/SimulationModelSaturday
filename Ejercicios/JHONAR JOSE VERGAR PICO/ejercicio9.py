inv = float(input("cantidad a invertir" ))
inta= float(input("interes anual "))
años = int(input("digite los años"))
print("capital final: " + str(round(inv * (inta /100 +1) ** años,2)))
