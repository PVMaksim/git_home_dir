
alfabet = [chr(i) for i in range(ord('а'), ord('а') + 32)]
data_input = 'тимур'
data1 = 'запретил букву'
txt = (data_input + ' ' + data1).split()
new_txt = ''
cnt = 0  # для нумерации в цикле while
str_text = 1  # счетчик подсчета напечатанных строк 1 так как первая строка печатается перед циклом


def del_char(text, char):  # удаление символа в тексте
    text = [i for i in text if i != char]
    return text


def len_different_letter(text):  # подсчет нужного количества строк
    kit_letter = []
    for c in text:
        if c not in kit_letter:
            kit_letter.append(c)
    return len(kit_letter)


# подсчет нужного количества строк
print(len_different_letter(data_input + data1))

print(' '.join(txt), alfabet[cnt])


# -1 так как в количестве строк (len_different_letter) есть один пробел
while str_text < len_different_letter(data_input + data1)-1:
    cnt += 1
    for i in txt:  # перебор слов
        new_txt += ''.join(del_char(i, alfabet[cnt-1]))  # удаляет буквы
        new_txt += ' '  # пробел между словами
    txt, new_txt = new_txt.split(), ''
    if alfabet[cnt] in ''.join(txt):
        print(' '.join(txt), alfabet[cnt])
        str_text += 1
        print(str_text, len_different_letter(data_input + data1)-1)
