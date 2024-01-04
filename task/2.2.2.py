namber = input().split()
cnt = 0
for i in range(1, len(namber)):
    if int(namber[i]) > int(namber[i-1]):
        cnt += 1
print(cnt)
