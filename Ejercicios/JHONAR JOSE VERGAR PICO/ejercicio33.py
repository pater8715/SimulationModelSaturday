materias = ["Matemáticas", " Fisica", " Quimica", " Historia", " lengua"]
notas = []
for materia in materias:
    nota = input("Que nota has sacado en " + materia)
    notas.append(nota)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + notas[i])