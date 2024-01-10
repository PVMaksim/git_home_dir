n = int(input())
k = [1, 1]  # соответствует 2 строке (n=2)
new_k = [1, 1]


def paskal(n):  # создает следующую строку пирамиды
    if n == 0:
        k = [1]
    elif n == 1:
        k = [1, 1]
    else:
        k = [1, 1]
        new_k = [1, 1]
        while len(k) <= n:
            for i in range(len(k)-1):
                new_k.insert(i + 1, k[i]+k[i + 1])
            k = [1, 1]
            k, new_k = new_k, k
    return k


print(paskal(n))
