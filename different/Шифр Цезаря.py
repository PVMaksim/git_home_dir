# запрос параметров у пользователя
print('Добро пожаловать в программу Шифр Цезаря')

en_alphabet = [chr(i) for i in range(ord('a'), ord('a') + 26)] + \
    [chr(i) for i in range(ord('A'), ord('A') + 26)]
ru_alphabet = [chr(i) for i in range(ord('а'), ord('а') + 32)] + [chr(i)
                                                                  for i in range(ord('А'), ord('А') + 32)]
ru_alphabet_low = [chr(i) for i in range(ord('а'), ord('а') + 32)]
en_alphabet_low = [chr(i) for i in range(ord('a'), ord('a') + 26)]


def togo():
    to_go = input(
        "Выбирете необходимые действия: 1 - шифрование 2 - дешифрование. Напишиие 1 или 2: ")
    while to_go not in '1, 2':
        to_go = input("Может всетаки выбетете 1 или 2: ")
    if int(to_go) == 1:
        print('Выбрано: шифрование')
        to_go = 1
        return to_go
    elif int(to_go) == 2:
        print('Выбрано: дешифрование')
        to_go = 2
        return to_go


# создал переменную с вривязкой к основной задаче программы
# (из функции достается только значение)
to_go = int(togo())

if to_go == 1:
    text_to_go = 'для шифрования'  # используется дальше в тексте для красаты
elif to_go == 2:
    text_to_go = 'для дешифрования'  # используется дальше в тексте для красаты


def language(text):
    print(f'Выбирете язык {text}', end='')
    language = input(
        ": 1 - Русский 2 - Inglesh. Напишиие 1 или 2: ")
    while language not in '1, 2':
        language = input("Может всетаки выбетете 1 или 2: ")
    if int(language) == 1:
        print('Выбран язык: Русский')
        language = 1
        return language
    elif int(language) == 2:
        print('Выбран язык: Inglesh')
        language = 2
        return language


language = int(language(text_to_go))
if language == 1:
    n_chars = 32  # общее количество символов в алфавите
elif language == 2:
    n_chars = 26  # общее количество символов в алфавите


def n_shift(text, n_chars):
    print(f'Выбирете параметр {text}', end=' ')
    n_shift = input(f'Напишите число от 1 до {n_chars}: ')
    while not n_shift.isdigit():
        n_shift = input(f"Напишите число от 1 до {n_chars}: ")
    while not 1 <= int(n_shift) <= n_chars:
        n_shift = input(f"Напишите число от 1 до {n_chars}: ")
    return n_shift


#  основная функция
# shift = int(n_shift(text_to_go, n_chars))


def code(shift, to_go, language):
    # input(f'Введите текст {text_to_go}: ')
    text = 'Hawnj pk swhg xabkna ukq nqj.'
    code_text = ''
    if language == 1:  # если Русский язык
        if to_go == 1:
            for i in text:
                if i in ru_alphabet:
                    if i in ru_alphabet_low:
                        # если  символ выходит из алфавита идем на второй круг по алфавиту
                        if (ord(i) + shift) >= ord('а') + n_chars:
                            code_text += chr(ord('а') + shift +
                                             (ord('а') + n_chars - 2 - ord(i)))
                        elif (ord(i) + shift) < ord('а') + n_chars:  # если  символ входит алфавит
                            code_text += chr(ord(i) + shift)
                    else:
                        if (ord(i) + shift) >= ord('А') + n_chars:
                            code_text += chr(ord('А') + shift +
                                             (ord('А') + n_chars - 2 - ord(i)))
                        elif (ord(i) + shift) < ord('А') + n_chars:  # если  символ входит алфавит
                            code_text += chr(ord(i) + shift)
                else:
                    code_text += i
            return code_text
        elif to_go == 2:
            for i in text:
                if i in ru_alphabet:
                    if i in ru_alphabet_low:
                        # если  символ выходит из алфавита идем на второй круг по алфавиту
                        if (ord(i) - shift) >= ord('а'):
                            code_text += chr(ord(i) - shift)
                        elif (ord(i) - shift) < ord('а'):  # если  символ входит алфавит
                            code_text += chr((ord('а') + n_chars -
                                              (ord(i) + 2 - ord('а') - shift)))
                    else:
                        # если  символ выходит из алфавита идем на второй круг по алфавиту
                        if (ord(i) - shift) >= ord('А'):
                            code_text += chr(ord(i) - shift)
                        elif (ord(i) - shift) < ord('А'):  # если  символ входит алфавит
                            code_text += chr((ord('А') + n_chars -
                                              (ord(i) + 2 - ord('А') - shift)))
                else:
                    code_text += i
            return code_text
    else:  # если английский язык
        print(sh)
        if to_go == 1:
            for i in text:
                if i in en_alphabet:
                    if i in en_alphabet_low:
                        # если  символ выходит из алфавита идем на второй круг по алфавиту
                        if (ord(i) + shift) >= ord('a') + n_chars:
                            code_text += chr(ord('a') +
                                             ((ord(i) + shift) - (ord('a') + n_chars)))
                            print((ord('a'), shift,
                                   (ord('a'), n_chars, '2', ord(i))))
                        elif (ord(i) + shift) < ord('a') + n_chars:  # если  символ входит алфавит
                            code_text += chr(ord(i) + shift)
                    else:
                        if (ord(i) + shift) >= ord('A') + n_chars:
                            code_text += chr(ord('A') +
                                             ((ord(i) + shift) - (ord('A') + n_chars)))
                        elif (ord(i) + shift) < ord('A') + n_chars:  # если  символ входит алфавит
                            code_text += chr(ord(i) + shift)
                else:
                    code_text += i
            return code_text
        elif to_go == 2:
            for i in text:
                if i in en_alphabet:
                    if i in en_alphabet_low:
                        # если  символ выходит из алфавита идем на второй круг по алфавиту
                        if (ord(i) - shift) >= ord('a'):
                            code_text += chr(ord(i) - shift)
                        elif (ord(i) - shift) < ord('a'):  # если  символ входит алфавит
                            code_text += chr((ord('a') + n_chars -
                                             (ord('a') - (ord(i) - shift))))
                    else:
                        # если  символ выходит из алфавита идем на второй круг по алфавиту
                        if (ord(i) - shift) >= ord('A'):
                            code_text += chr(ord(i) - shift)
                        elif (ord(i) - shift) < ord('A'):  # если  символ входит алфавит
                            code_text += chr((ord('A') + n_chars -
                                             (ord('A') - (ord(i) - shift))))
                else:
                    code_text += i
            return code_text


for i in range(0, 25):
    sh = i
    to_go = 2
    language = 2
    print(code(sh, to_go, language))


# code_text = ""
# shift = 1
# n_chars = 32
# i = 'я'
# я = ord(i) + shift
# if (ord(i) + shift) > ord('а') + n_chars:
#     code_text += chr(ord('а') + shift - ord(i))
# print(code_text)
