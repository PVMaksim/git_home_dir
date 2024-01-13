n = 2
matrix = []
mx = 0
for _ in range(n):
    tamp = [int(i) for i in input().split()]
    matrix.append(tamp)

for r in range(n):
    for c in range(n):
        if r <= c:
            if matrix[r][c] > mx:
                mx = matrix[r][c]
print(mx)
