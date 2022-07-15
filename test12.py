# 縦横に並ぶ数字の数を入力
size = int(input())

# ゲーム画面を行列で表現する
matrix = []
for i in range(size): # 行数に応じた繰り返し処理
  line = [int(e) for e in input().split()]
  matrix.append(line)

print(matrix)
