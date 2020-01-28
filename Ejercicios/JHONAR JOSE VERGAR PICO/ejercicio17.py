peso=input("Digite su peso (Kg) ")
estatura=input("Digite su estatura (Metros) ")
imc=round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es: "+ str(imc))