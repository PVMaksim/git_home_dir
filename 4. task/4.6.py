# n, m = [int(i) for i in input().split()]
n = 4
m = 5
matrix = [[0] * m for i in range(n)]
cnt = 0
for k in range(1):
    for i in range(n):
        for j in range(m):
            if i == k:
                matrix[i][j] = cnt+1
            cnt += 1
            # elif j == m-1:
            #     # c += 1
            #     matrix[i][j] = cnt+1
            #     cnt += 1
            # elif


for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
