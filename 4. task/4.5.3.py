n = int(input())
m = int(input())
mult = []
for _ in range(n):
    tamp = [int(i) for i in range(m)]
    mult.append(tamp)
# mult = [[0, 1, 3, 5],
#         [0, 1, 5, 7],
#         [0, 1, 5, 6]]
n_rows = input().split()


for r in range(1):
    for c in range(n):
        mult[c][int(n_rows[0])], mult[c][int(n_rows[1])
                                         ] = mult[c][int(n_rows[1])], mult[c][int(n_rows[0])]
        print(mult[c][1])
