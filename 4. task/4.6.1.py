n = 4
m = 1

matrix = [['.'] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 != 0:
            matrix[i][j] = '*'
        elif i % 2 != 0 and j % 2 == 0:
            matrix[i][j] = '*'
    print(*matrix[i])
