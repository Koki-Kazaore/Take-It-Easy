# 縦×横のサイズを入力し，sizeリストに格納
size = [int(e) for e in input().split()]

# 脱出ゲームの空間を行列で表現する
matrix = []
for i in range(size[0]): # 行数に応じた繰り返し処理
  line = list(input())
  # Sを見つけた時点でスタート位置の座標を格納しておく
  if 'S' in line:
    start_point = [i, line.index('S')]
  matrix.append(line)

# 現在の位置座標を取得(後に移動させるため，copyを用いる)
current_point = start_point.copy()
# スタート位置を0に置き換える(何度探索しているかをカウントするため)
matrix[start_point[0]][start_point[1]] = 0

while True:
  # 現在地の上下左右の位置座標を更新
  up = current_point[0] - 1
  down = current_point[0] + 1
  left = current_point[1] - 1
  right = current_point[1] + 1

  # 現在位置を追跡して確認するためのコード
  # print('現在位置', current_point)
  """
  # リストの中身のtypeを確認するためのコード
  for i in range(size[0]):
    for j in range(size[1]):
      print(type(matrix[i][j]), end="")
    print()
  """

  # 脱出ゲームの空間の端っこにいると判断された場合はYesと表示して終了
  if (up == -1) or (down == size[0]) or (left == -1) or (right == size[1]):
    print("YES")
    break

  # もし現在地の上に道があれば進み，進む前の位置の数をインクリメントする
  if matrix[up][current_point[1]] == '.':
    # 移動前の位置が'.'であった場合は0に置き換える
    if matrix[current_point[0]][current_point[1]] == '.':
      matrix[current_point[0]][current_point[1]] = 0
    else:
      matrix[current_point[0]][current_point[1]] += 1

    current_point[0] = up
  
  # もし現在地の下に道があれば進み，進む前の位置の数をインクリメントする
  elif matrix[down][current_point[1]] == '.':
    # 移動前の位置が'.'であった場合は0に置き換える
    if matrix[current_point[0]][current_point[1]] == '.':
      matrix[current_point[0]][current_point[1]] = int(0)
    else:
      matrix[current_point[0]][current_point[1]] += 1

    current_point[0] = down

  # もし現在地の左に道があれば進み，進む前の位置の数をインクリメントする
  elif matrix[current_point[0]][left] == '.':
    # 移動前の位置が'.'であった場合は0に置き換える
    if matrix[current_point[0]][current_point[1]] == '.':
      matrix[current_point[0]][current_point[1]] = 0
    else:
      matrix[current_point[0]][current_point[1]] += 1

    current_point[1] = left

  # もし現在地の右に道があれば進み，進む前の位置の数をインクリメントする
  elif matrix[current_point[0]][right] == '.':
    # 移動前の位置が'.'であった場合は0に置き換える
    if matrix[current_point[0]][current_point[1]] == '.':
      matrix[current_point[0]][current_point[1]] = 0
    else:
      matrix[current_point[0]][current_point[1]] += 1

    current_point[1] = right

  else:
    # print(matrix)
    # もし現在地の上に一度通った道があれば進み，進む前の位置の数をインクリメントする
    if matrix[up][current_point[1]] in range(0, 4):
      if matrix[current_point[0]][current_point[1]] == '.':
        matrix[current_point[0]][current_point[1]] = 0
      else:
        matrix[current_point[0]][current_point[1]] += 1
      current_point[0] = up

    # もし現在地の下に一度通った道があれば進み，進む前の位置の数をインクリメントする
    elif matrix[down][current_point[1]] in range(0, 4):
      if matrix[current_point[0]][current_point[1]] == '.':
        matrix[current_point[0]][current_point[1]] = 0
      else:
        matrix[current_point[0]][current_point[1]] += 1
      current_point[0] = down

    # もし現在地の左に一度通った道があれば進み，進む前の位置の数をインクリメントする
    elif matrix[current_point[0]][left] in range(0, 4):
      if matrix[current_point[0]][current_point[1]] == '.':
        matrix[current_point[0]][current_point[1]] = 0
      else:
        matrix[current_point[0]][current_point[1]] += 1
      current_point[1] = left

    # もし現在地の右に一度通った道があれば進み，進む前の位置の数をインクリメントする
    elif matrix[current_point[0]][right] in range(0, 4):
      if matrix[current_point[0]][current_point[1]] == '.':
        matrix[current_point[0]][current_point[1]] = 0
      else:
        matrix[current_point[0]][current_point[1]] += 1
      current_point[1] = right

    # 一度通った道をインクリメントしていき，その数が4以上になったらもうどうしようもないと判断し、終了
    else:
      print("NO")
      break

# テスト用コード
# print('縦横サイズ->', size)
# print('脱出ゲームの空間', matrix)
# print('スタート位置', start_point)