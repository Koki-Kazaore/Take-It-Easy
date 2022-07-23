# 縦×横のサイズと入力回数を入力し，input_lineリストに格納
input_line = [int(e) for e in input().split()]
height = input_line[0]
width = input_line[1]
trials = input_line[2]

# 盤面の状況を全て格納する
matrix = []
for i in range(height):
  row = [e for e in input()]
  matrix.append(row)

# 何行何列目の要素を取り出すのか
info = []
for times in range(trials):
  row = [int(e) for e in input().split()]
  info.append(row)

# print(info)


# 出力
for i in range(trials):
  x = info[i][0]
  y = info[i][1]
  print(matrix[x][y])
