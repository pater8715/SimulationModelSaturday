peso = input("cual es su peso en Kg ")
estatura = input("cual es su estatura en metros ")
imc = round(float(peso)/float(estatura)**2,2)
print("Su índice de masa corporal es: "+ str(imc))
