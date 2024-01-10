n = int(input())


def paskal(n):
    new_k = []
    k = [1]
    for _ in range(n-1):
        k = [0] + k + [0]
        for i in range(len(k)-1):
            new_k.append((k[i] + k[i+1]))
        print(*new_k)
        new_k, k = [], new_k


print(1)
paskal(n)
