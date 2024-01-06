
alfabet = [chr(i) for i in range(ord('а'), ord('а') + 32)]
data_input = 'тяимур'
txt = (data_input + ' ' + 'запретил букву').split()
new_txt = ''
cnt = 0  # для нумерации в цикле while


def del_char(text, char):  # удаление символа в тексте
    text = [i for i in text if i != char]
    return text


cnt2 = 1
print(' '.join(txt), alfabet[cnt])
while True:
    cnt += 1
    for i in txt:
        new_txt += ''.join(del_char(i, alfabet[cnt-1]))
        new_txt += ' '  # пробел между словами
    txt, new_txt = new_txt.split(), ''
    if alfabet[cnt] in ''.join(txt):
        cnt2 += 1
        print(' '.join(txt), alfabet[cnt], cnt2)
    if len(txt) <= 1:
        break
