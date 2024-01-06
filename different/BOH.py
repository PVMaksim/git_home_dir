n = int(input())
n_2 = bin(n)[2:]
n_8 = oct(n)[2:]
n_16 = hex(n)[2:].upper()
print(n_2, n_8, n_16, sep='\n')
