Timur = input()
Ruslan = input()

if Timur == Ruslan:
    print('ничья')
elif (Timur == 'ножницы' and Ruslan == 'бумага') or (Timur == 'камень' and Ruslan == 'ножницы')\
    or (Timur == 'бумага' and Ruslan == 'камень'):
    print('Тимур')
else:
    print('Руслан')
