caiv = float(input("cantidad a invertir " ))
intea= float(input("interes anual "))
años = int(input("digite los años "))
print("capital final: " + str(round(caiv * (intea /100 +1) ** años,2)))
