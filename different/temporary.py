n = input()
rezult = ''
while n != '0':
    rezult += ',' + n[:-4:-1]
    n = int(n) // 1000
    n = str(n)
print(rezult[:0:-1])
