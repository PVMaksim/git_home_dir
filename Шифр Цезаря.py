# запрос параметров у пользователя
print('Добро пожаловать в программу Шифр Цезаря')

en_alphabet = [chr(i) for i in range(ord('a'), ord('a') + 26)]
ru_alphabet = [chr(i) for i in range(ord('а'), ord('а') + 32)]


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


print(n_shift(text_to_go, n_chars))
