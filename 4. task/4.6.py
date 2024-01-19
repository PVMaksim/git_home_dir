# n, m = [int(i) for i in input().split()]
n = 4
m = 5
matrix = [[0] * m for i in range(n)]
spiral = 0
cnt = 0

for i in range(m):
    cnt += 1
    matrix[0][i] = cnt
i = 0
j = m-1

while cnt <= len(matrix)*len(matrix[0]):

    for c in range(n-1):  # вниз
        i += 1
        cnt += 1
        matrix[i][j] = cnt

    for c in range(m-1):  # влево
        cnt += 1
        j -= 1
        matrix[i][j] = cnt

    for c in range(n-1-1):  # вверх
        i -= 1
        cnt += 1
        matrix[i][j] = cnt

    for c in range(m-1-1):
        j += 1
        cnt += 1
        matrix[i][j] = cnt

    n -= 2
    m -= 2

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
