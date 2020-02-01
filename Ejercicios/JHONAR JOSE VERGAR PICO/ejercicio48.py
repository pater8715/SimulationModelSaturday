curso = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
total_creditos = 0
for subject, credits in curso.items():
    print(subject, 'tiene', credits, 'creditos')
    total_creditos += credits
print('nuemro total de creditos del curso: ', total_creditos) 