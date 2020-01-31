matriz_a = ((1, 2, 3),
     (4, 5, 6))
matriz_b = ((-1, 0),
     (0, 1),
     (1,1))
producto = [[0,0],
          [0,0]]
for i in range(len(matriz_a)):
    for j in range(len(matriz_b[0])):
        for k in range(len(matriz_b)):
            producto[i][j] += matriz_a[i][k] * matriz_b[k][j]
for i in range(len(producto)):
    producto[i] = tuple(producto[i])
producto = tuple(producto)
for i in range(len(producto)):
    print(producto[i])