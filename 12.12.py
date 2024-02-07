import random
import string

char_del = set('lI10oO')

char_A = set(string.ascii_uppercase) - char_del
char_a = set(string.ascii_lowercase) - char_del
char_1 = set(string.digits) - char_del
chars = (char_A | char_a | char_1) - char_del


def generate_password(length):
    password = (random.choice(list(char_A))
                + random.choice(list(char_a))
                + random.choice(list(char_1))
                + ''.join(random.sample(list(chars), length - 3)))

    return password


def generate_passwords(count, length):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords


# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')
