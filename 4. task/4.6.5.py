# n, m = [int(i) for i in input().split()]
n = 5
m = 7
matrix = []

for i in range(n):
    tamp = []
    for j in range(1, m+1):
        tamp.append(j)
    matrix.append(tamp)


for i in range(n):
    for j in range(m):
        if i % 2 != 0:
            matrix[i][j] = matrix[i-1][m-j-1] + m
        if i % 2 == 0 and i != 0:
            matrix[i][j] = matrix[i-1][m-j-1] + m

    # matrix.append(tamp)


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
