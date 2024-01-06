s = input().split()
cnt = 1
for i in range(len(s)-1):
    if s[i+1] != s[i]:
        cnt += 1
print(cnt)
