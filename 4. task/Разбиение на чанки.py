s = 'a b c d'.split()
n = int(input())


def chunked(text, number):
    rez = [[s.pop(0)]]
    for c in s:
        if len(rez[-1]) < n:
            rez[-1].append(c)
        else:
            rez.append([c])
    return rez


print(chunked(s, n))
