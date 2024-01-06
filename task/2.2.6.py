digits = [int(input()) for i in range(int(input()))]
n = int(input())
flag = 'НЕТ'
for i in range(len(digits)):
    for j in range(len(digits)):
        if i == j:
            continue
        if digits[i] * digits[j] == n:
            flag = 'ДА'
print(flag)
