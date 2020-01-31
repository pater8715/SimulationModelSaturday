vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
resul = 0
for i in range(len(vector1)):
    resul += vector1[i]*vector2[i]
print("El producto de los vectores" + str(vector1) + " y " + str(vector2) + " es " + str(resul)) 