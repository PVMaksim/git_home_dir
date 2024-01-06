number = int(input())
cnt = 0
rezult = []


def check_anton(text):
    anton = 'anton'
    index_a = text.find('a')
    if index_a != -1:
        for i in range(1, len(anton)):
            index_i = text.find(anton[i], index_a)
            if index_i != -1:
                index_i = text.find(anton[i], index_i)
                index_a = index_i
            else:
                return False
        return True
    else:
        return False


for _ in range(number):
    cnt += 1
    txt = input()
    if check_anton(txt):
        rezult += [cnt]

print(*rezult)
