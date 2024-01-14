n = int(input())
m = int(input())
ss = '2 5 6 5'
mult = []

for i in range(n):
    tamp = [int(i) for i in input().split()]
    mult.append(tamp)

for i in range(n):
    print(mult[i])

for i in range(n):
    for j in range(m):
        mx = mult[0][0]
        if mult[i][j] >= mx:
            mx = mult[i][j]
            i_j = (str(i)+' ' + str(j)).split()
print(*i_j)
