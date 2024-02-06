numbers = [int(i) for i in range(10)]
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
letters_numbers = letters + numbers
morze = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-.... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.'.split()
dict_morze = dict(zip(letters_numbers, morze))
txt = 'aab'.lower()

print(*[dict_morze[char] + ' ' for char in txt if char in dict_morze])
