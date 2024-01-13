n = int(input())
ss = '1 2 5'
matrix = []
sm1 = []
sm2 = []
sm3 = []
sm4 = []
for _ in range(n):
    tamp = [int(i) for i in input().split()]
    matrix.append(tamp)
for i in range(n):
    print(matrix[i])

for i in range(n):
    for j in range(n):
        if i < j and i < (n - j - 1):
            sm1.append(matrix[i][j])
        elif i < j and i > (n - j - 1):
            sm2.append(matrix[i][j])
        elif i > j and i > (n - j - 1):
            sm3.append(matrix[i][j])
        elif i > j and i < (n - j - 1):
            sm4.append(matrix[i][j])

print('Верхняя четверть:', sum(sm1))
print('Правая четверть:', sum(sm2))
print('Нижняя четверть:', sum(sm3))
print('Левая четверть:', sum(sm4))
