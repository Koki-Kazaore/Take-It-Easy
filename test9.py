# 縦×横のサイズを入力し，sizeリストに格納
size = [int(e) for e in input().split()]

# 板の並んでいる状況を行列で表現する
matrix = []
for i in range(size[0]): # 行数に応じた繰り返し処理
  line = [int(e) for e in input().split()]
  matrix.append(line)

# 最大値を格納する変数
points = 0
# 現在いる位置を把握するための変数
current_row = 0
current_column = 0

# 同じ比較範囲内に同じ数値があったかどうかを判定する
conflict = False


# 最終行に達するまでpointsを加えていく処理
while current_row < size[0]:
  # 初期値の最大値の選び方
  if current_row == 0:
    max_point = max(matrix[0][:])
    current_column = matrix[0].index(max_point)
    points += max_point

    # 同じ比較範囲内に同じ数値があったかどうかの判定
    if matrix[0][:].count[max_point] != 1:
      conflict = True
      matrix[0][current_column] -= 1
    else:
      conflict = False

    # check program
    print("max_point->", max_point)
    print("current_column->", current_column)

  # 2行目以降の処理
  else:
    # i行の左右範囲の中で最大値を探す
    print("current_row->", current_row)
    print("range_left:range_right ==", range_left, ":", range_right)
    max_point = max(matrix[current_row][range_left:range_right])

    # 同じ比較範囲内に同じ数値があったかどうかの判定
    if matrix[current_row][:].count[max_point] != 1:
      conflict = True
      matrix[0][current_column] -= 1
    else:
      conflict = False

    # 移動する変化量を求め、グローバル変数のcurrent_culmunを更新
    move = matrix[current_row][range_left:range_right].index(max_point) - 1
    current_column += move
    print("after current_column->", current_column)
    points += max_point


  # 次の行で最大値を探す範囲を決定する
  range_left = current_column - 1
  range_right = current_column + 2
  # 0列目よりも左に設定されてしまった場合は0にしてしまう
  if current_column <= 0:
    range_left = 0
  # 列数より大きい値に設定されてしまった場合は列の最後までに調整する
  if current_column >= size[1] - 1:
    range_right = current_column + 1

  # 次の行について処理を行うため、インクリメントする
  current_row += 1



# 確認用プログラム
print("size->", size)
print("matrix->", matrix)

print(points)