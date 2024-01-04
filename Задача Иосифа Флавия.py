
n = int(input())  # количество людей
k = int(input())  # номер человека который выбывает


def namber_kill():
    namber = [i for i in range(1, n+1)]
    new_namber = []
    cnt = 0
    while len(namber) != 1:
        cnt += 1
        if cnt != k:
            namber += [namber[0]]
            namber.pop(0)
        else:
            del namber[0]
            cnt = 0
    return namber


print(*namber_kill())
