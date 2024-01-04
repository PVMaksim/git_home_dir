n = int(input())

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        cnt1 += 1
    elif x < 0 and y > 0:
        cnt2 += 1
    elif x < 0 and y < 0:
        cnt3 += 1
    elif x > 0 and y < 0:
        cnt4 += 1
print('Первая четверть:', cnt1)
print('Вторая четверть:', cnt2)
print('Третья четверть:', cnt3)
print('Четвертая четверть:', cnt4)
