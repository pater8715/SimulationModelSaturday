weight = input ("¿Cual es tu peso en Kg? ")
height = input ("¿Cual es tu estatura en Metros?")
bmi = round(float(weight)/float(height)**2,2)
print ("Tu indice de masa corporal es " + str(bmi))