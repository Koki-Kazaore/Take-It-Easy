import sys

# 縦横に並ぶ数字の数を入力
size = int(input())

# ゲーム画面を行列で表現する
matrix = []
for i in range(size): # 行数に応じた繰り返し処理
  line = [int(e) for e in input()]
  matrix.append(line)

# 最大値を格納する変数
swipes = 0
# 現在いる位置を把握するための変数
current_row = 0
current_column = 0

flag = False

"""まずは隣接する値が1つ上昇する場合のみを考える"""
# スタート地点をループで回す
for i in range(0, size - 1): # 最終行をスタート地点にする必要は無い
  current_row = i
  if flag == True:
    break

  for j in range(0, size):
    # 最大値が自明な場合は強制終了
    if swipes == size:
      print(swipes)
      flag = True
      break

    temp_swipes = 1
    current_column = j
    # スタート地点の初期値
    initial_value = matrix[i][j]
    """スタート地点が左端の場合"""
    if j == 0:
      # 右へ進む
      for next_right in range(j + 1, size):
        # 前回値より1大きい場合
        if matrix[current_row][next_right - 1] == matrix[current_row][next_right] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes  

      # 初期化
      temp_swipes = 1     

      # 下へ進む
      for next_down in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[next_down - 1][current_column] == matrix[next_down][current_column] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

      # 右下へ進む
      for buttom_right in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_right - 1][buttom_right - 1] == matrix[buttom_right][buttom_right] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

    """スタート地点が右端の場合"""
    if j == size - 1:
      # 下へ進む
      for next_down in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[next_down - 1][current_column] == matrix[next_down][current_column] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

      # 左下へ進む
      total = i + j
      for buttom_left in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_left - 1][total - buttom_left + 1] == matrix[buttom_left][total - buttom_left] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

    """端以外の任意のスタート地点の場合"""
    if j != 0 and j != size - 1:
      # 右へ進む
      for next_right in range(j + 1, size):
        # 前回値より1大きい場合
        if matrix[current_row][next_right - 1] == matrix[current_row][next_right] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes  

      # 初期化
      temp_swipes = 1

      # 下へ進む
      for next_down in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[next_down - 1][current_column] == matrix[next_down][current_column] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

      # 右下へ進む
      for buttom_right in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_right - 1][buttom_right - 1] == matrix[buttom_right][buttom_right] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

    # 左下へ進む
      total = i + j
      for buttom_left in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_left - 1][total - buttom_left + 1] == matrix[buttom_left][total - buttom_left] - 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1


"""次に隣接する値が1つ下がる場合のみを考える"""
# スタート地点をループで回す
for i in range(0, size - 1): # 最終行をスタート地点にする必要は無い
  current_row = i
  if flag == True:
    break

  for j in range(0, size):
    # 最大値が自明な場合は強制終了
    if swipes == size:
      print(swipes)
      flag = True
      break

    temp_swipes = 1
    current_column = j
    # スタート地点の初期値
    initial_value = matrix[i][j]
    """スタート地点が左端の場合"""
    if j == 0:
      # 右へ進む
      for next_right in range(j + 1, size):
        # 前回値より1大きい場合
        if matrix[current_row][next_right - 1] == matrix[current_row][next_right] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes  

      # 初期化
      temp_swipes = 1     

      # 下へ進む
      for next_down in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[next_down - 1][current_column] == matrix[next_down][current_column] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

      # 右下へ進む
      for buttom_right in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_right - 1][buttom_right - 1] == matrix[buttom_right][buttom_right] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

    """スタート地点が右端の場合"""
    if j == size - 1:
      # 下へ進む
      for next_down in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[next_down - 1][current_column] == matrix[next_down][current_column] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

      # 左下へ進む
      total = i + j
      for buttom_left in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_left - 1][total - buttom_left + 1] == matrix[buttom_left][total - buttom_left] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

    """端以外の任意のスタート地点の場合"""
    if j != 0 and j != size - 1:
      # 右へ進む
      for next_right in range(j + 1, size):
        # 前回値より1大きい場合
        if matrix[current_row][next_right - 1] == matrix[current_row][next_right] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes  

      # 初期化
      temp_swipes = 1

      # 下へ進む
      for next_down in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[next_down - 1][current_column] == matrix[next_down][current_column] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

      # 右下へ進む
      for buttom_right in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_right - 1][buttom_right - 1] == matrix[buttom_right][buttom_right] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1

    # 左下へ進む
      total = i + j
      for buttom_left in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_left - 1][total - buttom_left + 1] == matrix[buttom_left][total - buttom_left] + 1:
          temp_swipes += 1
        else:
          break

      if temp_swipes > swipes:
        swipes = temp_swipes

      # 初期化
      temp_swipes = 1



# print(matrix)
if flag == False:
  print(swipes)
