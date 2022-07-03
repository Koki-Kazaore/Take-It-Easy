# ttt

# 縦×横のサイズを入力し，sizeリストに格納
size = [int(e) for e in input().split()]

# 板の並んでいる状況を行列で表現する
matrix = []
for i in range(size[0]): # 行数に応じた繰り返し処理
  line = [int(e) for e in input().split()]
  matrix.append(line)

# 最大値を格納する変数
points = 0
temp_poit = 0

# 現在いる位置を把握するための変数
current_row = 0
current_column = 0


for i in range(size[1]): # iは現在の列(column)を示す示す
  temp_poit += matrix[0][i]

  # 次の行で最大値を探す範囲を決定する
  range_left = max(0, i - 1)
  range_right = min(size[1], i + 2)

  # iiは次の範囲内の列を示す
  for ii in range(range_left, range_right):
    current_row = 1
    
  

# 1行目の1要素全てのパターンのみ考える
for i in range(0, size[0]):
  for j in range(range_left, range_right):









while current_column < size[1]:
  point = matrix[0][current_column]

  for i in range(range_left, range_right):



  # 次の行で最大値を探す範囲を決定する
  range_left = max(0, current_column - 1)
  range_right = min(size[1], current_column + 2)
  

  # 次の行について処理を行うため、インクリメントする
  current_row += 1