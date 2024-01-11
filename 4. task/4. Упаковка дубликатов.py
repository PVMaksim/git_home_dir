
lst = input().split()

rez = [lst.pop(0)]
print(rez, lst)
for i in range(len(lst)):
    char = lst.pop(0)
    if char not in rez[-1]:
        rez += [list(char)]
    else:
        rez[-1] += [char]
print(rez)
