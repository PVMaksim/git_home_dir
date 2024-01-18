# n, m = [int(i) for i in input().split()]
n = 4
m = 4

matrix = []
for i in range(n):
    tamp = []
    for j in range(m):
        if i <= j and i + j + 1 <= n:
            tamp.append(1)
        elif i >= j and i + j + 1 >= n:
            tamp.append(1)
        else:
            tamp.append(0)
    matrix.append(tamp)

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
