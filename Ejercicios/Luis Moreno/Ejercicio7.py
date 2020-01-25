weight = input("¿Cual es tu peso en kg? ")
height = input("¿Cual es tu estatura en metros?")
bmi = round(float(weight)/float(height)**2,2)
print("Tu indice de masa corporal es " + str(bmi))