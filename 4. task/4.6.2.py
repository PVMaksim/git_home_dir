n = 5
matrix = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == n-j-1:
            matrix[i][j] = 1
        if i > n - j-1:
            matrix[i][j] = 2
for i in range(n):
    print(matrix[i])
