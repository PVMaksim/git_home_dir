position = 'c1'
position_cols_N = ord(position[0]) - ord('a')
position_rows_N = 8 - int(position[1])  # так как отсчет в шахматах с 1
n = 8
chess = [['.'] * 8 for _ in range(n)]
abc = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chess[position_rows_N][position_cols_N] = 'N'
optios = [[2, 1],
          [2, -1],
          [-2, 1],
          [-2, -1],
          ]

for i in range(4):
    position_rows = position_rows_N + optios[i][0]
    position_cols = position_cols_N + optios[i][1]
    if 0 <= position_rows < 8 and 0 <= position_cols < 8:
        chess[position_rows][position_cols] = '*'
    position_rows = position_rows_N + optios[i][1]
    position_cols = position_cols_N + optios[i][0]
    if 0 <= position_rows < 8 and 0 <= position_cols < 8:
        chess[position_rows][position_cols] = '*'
print(*abc)
for i in range(len(chess)):
    print(8 - i, *chess[i])
