n = 2
matrix = []
total = 0

for i in range(n):
    matrix.append(input().split())

print(matrix)

for i in range(n):
    for j in range(n):
        if i == j:
            total += int(matrix[i][j])

print(total)
