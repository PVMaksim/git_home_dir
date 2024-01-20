# n, m = [int(i) for i in input().split()]
n = 4
m = 8
matrix = [[0] * m for i in range(n)]

cnt = 1

i = 0
j = -1

d_row = 0
d_cols = 1
while cnt != m*n+1:
    if 0 <= i+d_row <= n-1 and 0 <= j+d_cols <= m-1 and matrix[i+d_row][j+d_cols] == 0:
        i = i + d_row
        j = j + d_cols
        matrix[i][j] = cnt
        cnt += 1
    else:
        if d_cols == 1:  # если шли вправо
            d_cols = 0
            d_row = 1
        elif d_row == 1:  # если шли вниз
            d_row = 0
            d_cols = -1
        elif d_cols == -1:  # если шли влево
            d_cols = 0
            d_row = -1
        elif d_row == -1:  # если шли вверх
            d_row = 0
            d_cols = 1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
