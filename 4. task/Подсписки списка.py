s = 'a b c d'.split()


rez = [[]]
for i in range(len(s)):
    char = []
    for j in range(len(s)):
        char += [s[j]]
        rez += [char[:]]
    s.pop(0)
rez.sort(key=len)
print((rez))
