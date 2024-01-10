s = 'a b b b c d'
lst = s.split()

rez = []
rez_2 = []


while len(lst) > 1:

    elem = lst[0]
    new_elem = lst[1]
    if new_elem != elem:
        rez += [list(elem)]
        lst.pop(0)
    elif new_elem == elem:
        while new_elem == elem:
            rez += [list(elem)]
            rez[-1] += (list(elem))
            lst.pop(0)
            elem = lst[0][0]
            new_elem = lst[1]
            if new_elem != elem:
                continue
            elif new_elem == elem:
                rez[-1] += (list(elem))
                lst.pop(0)

    print(rez)
