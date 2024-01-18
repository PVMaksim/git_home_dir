n = 3
# matrix = [input().split() for i in range]
new_matrix = [[0]*3 for i in range(n)]

matrix = [[1, 2, 3],
          [5, 5, 6],
          [4, 4, 4]]

for i in range(3):
    for j in range(n):
        new_matrix[i][j] = matrix[n-j-1][i]
        new_matrix[j][n-i-1] = matrix[i][j]
        new_matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
        new_matrix[n-j-1][i] = matrix[n-i-1][n-j-1]

        # rows = matrix[i][j]
        # cows = matrix[j][n-i-1]
for i in range(n):
    print(*matrix[i])
for i in range(n):
    print(*new_matrix[i])
