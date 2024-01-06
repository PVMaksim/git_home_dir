def from_10_in_sistem_base():
    n_10 = int(input("введите число в десятичной системе счисления: "))
    base = int(
        input("введите число в системы счисления в которую надо перевести: "))
    ABC = '0123456789ABCDEF'
    remains = []  # остаток
    if base == 16:
        while True:
            n = n_10 // base
            remains += ABC[n_10 % base]
            n_10 = n
            if n < base:
                break
        rezult = ''.join([str(i) for i in ([ABC[n]] + remains[::-1])])
        return rezult
    else:
        while True:
            n = n_10 // base
            remains += [n_10 % base]
            n_10 = n
            if n < base:
                break
        rezult = ''.join([str(i) for i in ([ABC[n]] + remains[::-1])])
        return rezult


print(from_10_in_sistem_base())
