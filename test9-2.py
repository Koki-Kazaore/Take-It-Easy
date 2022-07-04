# 縦×横のサイズを入力し，sizeリストに格納
size = [int(e) for e in input().split()]

# 板の並んでいる状況を行列で表現する
matrix = []
for i in range(size[0]): # 行数に応じた繰り返し処理
  line = [int(e) for e in input().split()]
  matrix.append(line)

# matrixリストが1行になるまでループを回す
while (len(matrix) != 1):

  # 各列における試行を記述する
  # 2行目と1行目を比較して和を求めていく
  for j in range(0, size[1]):
    # 一番左の要素の場合
    if j == 0:
      matrix[1][0] += max(matrix[0][0], matrix[0][1])
    # 一番右の要素の場合
    elif j == size[1] - 1:
      matrix[1][j] += max(matrix[0][j - 1], matrix[0][j])
    else:
      matrix[1][j] += max(matrix[0][j - 1], matrix[0][j], matrix[0][j + 1])

  # 1行目と2行目との和の演算が終了したら1行目を削除しておく
  del matrix[0]

# 最終的に残った最終行の要素の最大値を出力
print(max(matrix[0]))