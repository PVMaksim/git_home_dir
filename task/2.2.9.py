s = input()
cnt = 1
max_P = 0
for i in range(len(s)-1):
    if 'Р' not in s:
        print('0')
    elif s[i] == 'Р' and s[i+1] == 'Р':
        cnt += 1
    elif s[i] == 'Р' and s[i+1] != 'Р':
        if max_P < cnt:
            max_P = cnt
            cnt = 1
        else:
            cnt = 1
print(max_P)
