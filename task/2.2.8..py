Тимур = input()
Руслан = input()
lst = ['каменьножницы', 'ножницыбумага', 'бумагакамень', 'Споккамень',
       'ножницыящерица', 'ящерицабумага', 'ящерицаСпок', 'каменьящерица']
summ = Тимур + Руслан
if summ in lst:
    print('Тимур')
elif Тимур == Руслан:
    print('ничья')
else:
    print('Руслан')
