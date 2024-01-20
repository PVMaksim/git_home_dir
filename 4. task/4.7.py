# n, m = [int(i) for i in input().split()]
n = 4
m = 1

mas_a = [[int(j) for j in (input().split())] for _ in range(n)]
print()
mas_b = [[int(j) for j in (input().split())] for _ in range(n)]


mas_c = [[0]*m for _ in range(n)]
# mas_c =
for i in range(n):
    for j in range(m):
        mas_c[i][j] = mas_a[i][j] + mas_b[i][j]

for i in range(n):
    for j in range(m):
        print(str(mas_c[i][j]).ljust(3), end=' ')
    print()
