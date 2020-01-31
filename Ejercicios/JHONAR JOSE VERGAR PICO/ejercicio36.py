asignatura = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
flotante = []
for materia in asignatura:
    nota = float(input("¿Qué nota has sacado en " + materia + "?"))
    if nota >= 5:
        flotante.append(materia)
for materia in flotante:
    asignatura.remove(materia)
print("Tienes que repetir " + str(asignatura))