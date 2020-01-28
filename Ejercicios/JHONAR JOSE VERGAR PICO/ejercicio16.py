renta = float(input("Digite su renta anual "))
if renta < 10000:
    impo=5
elif renta < 20000:
    impo=15
elif renta < 35000:
    impo=20
elif renta < 60000:
    impo=30
else:
    impo=45
print(" tu tipo de impositivo es "+ str(impo) + "%")
  