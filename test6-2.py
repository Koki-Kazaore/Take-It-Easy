import itertools
import sys
import copy


# 2つのリストで要素の引き算をする関数
# 要素数がlist1 >= list2として利用する
# 直感的にはlist1 - list2
def subtranction(list1, list2):
  for i in list2:
    if i in list1:
      list1.remove(i)
  return list1


# 分銅の数を入力
count = int(input())

# 分銅の重さを入力
# 後のループ文をできるだけ早く終わらせるため、降順にソートしておく
weight = sorted([int(e) for e in input().split()], reverse=True)
# 以下でweightを書き換えることがあるため、コピーを取っておく
backup = copy.copy(weight)
# output確認用プログラム
# print('ソートされたweightリスト->', weight)
# print('set(weight)による集合->', set(weight))

# 仮の最小値をグローバル変数として決定しておく
minimum = 2048

# nCrの組み合わせを計算する上でのrの範囲を決定する
# weightリストの要素数の半分までで問題ない
for r in range(1, int(len(weight) / 2) + 1):

  # weightリストにおいてr個の組み合わせとその残りを計算する
  for left in itertools.combinations(weight, r):
    left = list(left)
    right = subtranction(weight, left)

    # output確認用プログラム
    # print(left, right)

    # 左の分銅の重さ
    left_weight = sum(left)
    # 右の分銅の重さ
    right_weight = sum(right)

    if (left_weight == right_weight):
      print(0)
      sys.exit()
    else:
      diff = abs(left_weight - right_weight)
      if (diff < minimum):
        minimum = diff

    # 要素がremoveされているweightリストをリセットする。
    weight = copy.copy(backup)

# 最小値の出力
print(minimum)