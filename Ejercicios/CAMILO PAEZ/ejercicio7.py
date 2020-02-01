weight = input("¿cual es tu peso en kg? ")
height = input("¿cual es tu estatura en metros ?")
bmi = round(float(weight)/float(height)**2,2)
print("Tu indice de masa corporal es " + str(bmi))