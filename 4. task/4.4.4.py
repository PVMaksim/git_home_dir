# n = int(input())
n = 5
maxrix = [[5, 3, 7, 1, 5],
          [3, 5, 4, 5, 7],
          [7, 4, 4, 8, 4],
          [1, 5, 8, 5, 1],
          [5, 7, 4, 1, 5]]
# maxrix = [input().split() for i in range(n)]
i_more_j = []
j_more_i = []

for i in range(n):
    i_more_j.append('*')
    j_more_i.append('*')
    tamp_i = []
    tamp_j = []
    for j in range(n):
        tamp_i.append(maxrix[j][i])
        tamp_j.append(maxrix[i][j])

    i_more_j.append(tamp_i[i+1:])
    j_more_i.append(tamp_j[i+1:])

print(i_more_j)
print(j_more_i)
if i_more_j == j_more_i:
    print('YES')
else:
    print('NO')
