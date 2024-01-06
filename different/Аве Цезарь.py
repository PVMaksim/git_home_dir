text = input().split()


alfabet_low = [chr(i) for i in range(ord('a'), ord('a') + 26)] * 2
alfabet_upp = [chr(i) for i in range(ord('A'), ord('A') + 26)] * 2


def code(text):
    code = []
    onle_txt = [i for i in text if i in alfabet_low + alfabet_upp]
    for i in text:
        if i in alfabet_low:
            index_i = alfabet_low.index(i) + len(onle_txt)
            code.append(alfabet_low[index_i])
        elif i in alfabet_upp:
            index_i = alfabet_upp.index(i) + len(onle_txt)
            code.append(alfabet_upp[index_i])
        else:
            code.append(i)
    str_code = ''.join(code)
    return str_code


shift_lst = ''

for i in text:
    shift_lst += ''.join(code(i))
    shift_lst += ' '
print(shift_lst)
