nombre = input("como te llamas ")
sexo = input("cual es tu sexo (M o H)")
if sexo == "M":
    if nombre.lower() < "m" :
        grupo = "A"
    else:
        grupo= "B"
else:
    if nombre.lower() > "n" :
        grupo = "A"
    else:
        grupo= "B"
print("tu grupo es " + grupo)