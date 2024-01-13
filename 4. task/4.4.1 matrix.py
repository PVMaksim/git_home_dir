rows = int(input())
cols = int(input())
matrix = []

for i in range(rows):
    tamp = [input()for i in range(cols)]
    matrix.append(tamp)

for i in range(rows):
    for j in range(cols):
        print(*matrix[i][j], end=' ')
    print()
