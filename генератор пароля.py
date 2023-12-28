from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
dell_chars = "il1Lo0O"
costom_setting = True  # Стандартные ностройки


def standard_settings():  # "настройки для пароля:"
    dop_parametr = []
    n_pasword = 1  # 1 "необходимее количество паролей "
    len_pasword = 10  # 2 "количество символов в пароле "
    gigit_pasword = True  # 3 "добавлянм цифры в пароль "
    low_chars = True  # 4 "добавляем строчные буквы "
    upper_chars = True  # 5 "добавляем заклавные буквы "
    chars_in_pasword = True  # 6 "добавляем символы "
    dell_chars = True  # 7 "исключаем неоднозначные симвелы "
    return dop_parametr, n_pasword, len_pasword, gigit_pasword, low_chars, upper_chars, chars_in_pasword, dell_chars


def n_pasword(costom_setting):  # количество паролей
    if costom_setting == True:
        return standard_settings()[1]
    else:
        print('Количество паролей для генерации. Введите число от 1 до 10: ')
        cnt = 0
        while True:
            n_pasword = input()
            if n_pasword.isdigit() and 1 <= int(n_pasword) <= 10:
                return n_pasword
                break
            else:
                cnt += 1
                print('введите число от 1 до 10')
                if cnt == 2:
                    print('принято стандартное количества генераций пароля - ',
                          standard_settings()[1])
                    n_pasword = standard_settings()[1]
                    return n_pasword


def len_pasword(costom_setting):  # количество символов
    if costom_setting == True:
        return standard_settings()[2]
    else:
        print('Давайте определим сколька символав должно быть в пороле. Введите число от 6 до 20')
        cnt = 0
        while True:
            len_pasword = input()
            if len_pasword.isdigit() and 6 <= int(len_pasword) <= 20:
                return len_pasword
                break
            else:
                print('введите число от 6 до 20')
                cnt += 1
                if cnt == 2:
                    print('принято стандартное число символов - ',
                          standard_settings()[2])
                    len_pasword = standard_settings()[2]
                    return len_pasword


def gigit_pasword(costom_setting):  # нужноли добавить цифры в пароль
    if costom_setting == True:
        return standard_settings()[3]
    else:
        print("Включать ли цифры в пароль?. Введите да или нет ")
        cnt = 0
        while True:
            gigit_pasword = input()
            if gigit_pasword.lower() == "да":
                gigit_pasword = True
                return gigit_pasword
                break
            else:
                print('Вы хотите включать цифры в пороль?. Введите да или нет "')
                cnt += 1
                if cnt == 2:
                    print('Цифры не включаем в пароль')
                    gigit_pasword = False
                    return gigit_pasword


def low_chars(costom_setting):  # добавляем строчные буквы?
    if costom_setting == True:
        return standard_settings()[4]
    else:
        print('Нужно включить строчные буквы в пороль. Введите да или нет ')
        cnt = 0
        while True:
            low_chars = input()
            if low_chars.lower() == "да":
                return True
                break
            else:
                print(
                    'Вы хотите включить строчные буквы в пороль?. Введите да или нет "')
                cnt += 1
                if cnt == 2:
                    print('Строчные буквы не включаем в пароль')
                    return False


def upper_chars(costom_setting):  # добавляем заглавные буквы?
    if costom_setting == True:
        return standard_settings()[5]
    else:
        print('Нужно включить заглавные буквы в пороль. Введите да или нет ')
        cnt = 0
        while True:
            upper_chars = input()
            if upper_chars.lower() == "да":
                return True
                break
            else:
                print(
                    'Вы хотите включить заглавные буквы в пороль?. Введите да или нет "')
                cnt += 1
                if cnt == 2:
                    print('Заглавные буквы не включаем в пароль')
                    return False


def chars_in_pasword(costom_setting):
    if costom_setting == True:
        return standard_settings()[6]
    else:
        print('Нужно включить дополнительные символы (!#$%&*+-=?@^_?) в пороль. Введите да или нет ')
        cnt = 0
        while True:
            chars_in_pasword = input()
            if chars_in_pasword.lower() == "да":
                return True
                break
            else:
                print(
                    'Вы хотите включить дополнительные символы (!#$%&*+-=?@^_?) в пороль?. Введите да или нет "')
                cnt += 1
                if cnt == 2:
                    print(
                        'дополнительные символы (!#$%&*+-=?@^_?) не включаем в пароль')
                    return False


def dell_chars(costom_setting):  # Исключать ли неоднозначные символы il1Lo0O?
    if costom_setting == True:
        return standard_settings()[7]
    else:
        print('Исключать ли неоднозначные символы (il1Lo0O) из пороля? Введите да или нет ')
        cnt = 0
        while True:
            dell_chars = input()
            if dell_chars.lower() == "да":
                return True
                break
            else:
                print(
                    'Вы хотите исключить неоднозначные символы из пороля?. Введите да или нет "')
                cnt += 1
                if cnt == 2:
                    print('неоднозначные символы оставляем в пароле')
                    return False


def Yes_or_No(funthion):
    if funthion == True:
        return 'да'
    else:
        return 'нет'


def data():
    print("Стандартные настройки для пароля:", '\n',
          "необходимее количество паролей - ", standard_settings()[1], '\n'
          "количество символов в пароле - ", standard_settings()[2], '\n'
          "добавляем строчные буквы - ", Yes_or_No(
              low_chars(costom_setting)), '\n'
          "добавляем заклавные буквы - ", Yes_or_No(
              upper_chars(costom_setting)), '\n',
          "добавляем символы - ", Yes_or_No(
              chars_in_pasword((costom_setting))), '\n',
          "исключаем неоднозначные симвелы - ", Yes_or_No(
              dell_chars((costom_setting))), '\n',
          "",
          "Хотите изменить настройки пароля? Напишите да или нет", sep='')
    change_setting = input()
    if change_setting == 'да':
        change_setting = True
        return change_setting
    else:
        change_setting = False
        return change_setting

# основная программа
def generat_pasword():
    pasword = ''
    if data() == False:
        costom_setting = True
        charses = digits + lowercase_letters + uppercase_letters + punctuation
        for _ in range(standard_settings()[1]):
            for _ in range(standard_settings()[2]):
                pasword += choice(charses)
            print(pasword, len(pasword))
    else:
        costom_setting = False
        n_pasword(costom_setting)
        len_pasword(costom_setting)
        gigit_pasword(costom_setting)
        low_chars(costom_setting)
        upper_chars(costom_setting)
        chars_in_pasword(costom_setting)
        dell_chars(costom_setting)
    charses = ''
    if gigit_pasword(costom_setting) == True:
        charses += digits
    else:
        charses = ''
    if low_chars(costom_setting) == True:
        charses += low_chars
    else:
        charses = ''
    if upper_chars(costom_setting) == True:
        charses += upper_chars
    else:
        charses = ''
    if chars_in_pasword(costom_setting) == True:
        charses += punctuation
    else:
        charses = ''
    if dell_chars(costom_setting) == False:
        charses += dell_chars
    else:
        charses = ''
    if charses == '':
        print('Вы не выбрали не одного символа для составления пароля. Пароль будет создан только из цифр')
    charses += digits
    for _ in range(len_pasword(costom_setting)):
        pasword += choice(charses)
    print(pasword)


generat_pasword()
