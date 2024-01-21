# n, m = [int(i) for i in input().split()]
n = 3
m = 2

# mas_a = [[int(j) for j in (input().split())] for _ in range(n)]
mas_a = [[2, 5],
         [6, 7],
         [1, 8]]

print()
# m, k = [int(i) for i in input().split()]
m = 2
k = 3

# mas_b = [[int(j) for j in (input().split())] for _ in range(n)]
mas_b = [[1, 2, 1],
         [0, 1, 0]]

mas_c = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            mas_c[i][j] += mas_a[i][x] * mas_b[x][j]

for i in range(n):
    for j in range(k):
        print(str(mas_c[i][j]).ljust(3), end=' ')
    print()
