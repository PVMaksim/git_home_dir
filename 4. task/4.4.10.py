n = 3
# matrix = []
# for _ in range(n):
#     tamp = [int(i) for i in input().split()]
#     matrix.append(tamp)
flag = 'YES'
m = [3, 8, 1, 2, 4, 6, 7, 0, 5]
matrix = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]
sm = sum(matrix[0])
m.sort()

for i in range(1, len(m) - 1):
    if m[0] > 0:
        if m[i] + 1 == m[i+1]:
            flag = 'NO'

if flag != 'NO':
    diag = []
    diag2 = []
    for i in range(n):
        cols = []
        rows = []
        for j in range(n):
            cols += [matrix[j][i]]
            rows += [matrix[i][j]]
            if i == j:
                diag += [matrix[i][j]]
            if i == n - j-1:
                diag2 += [matrix[i][j]]
        if sum(rows) != sm:
            flag = 'NO'
        elif sum(cols) != sm:
            flag = 'NO'
        if flag == 'NO':
            break
if flag != 'NO':
    if sum(diag) != sm:
        flag = 'NO'
    elif sum(diag2) != sm:
        flag = 'NO'

print(flag)


# for i in range(n):
#     print(matrix[i])
