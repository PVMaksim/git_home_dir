import random
s = ['Светлана Зуева', 'Аркадий Белых', 'Борис Боков']

my_set = {s[i]: i for i in range(len(s))}
cnt = 0
while cnt <= len(my_set):
    for key in my_set:
        char = s.pop(s.index(random.choice(s)))
        while key == char:
            s += [char]
            break
        if key != char:
            my_set[key] = char
            cnt += 1

for k, v in my_set.items():
    print(f'{k} - {v}')
