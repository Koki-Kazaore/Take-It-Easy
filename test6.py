import itertools
import sys

"""
# 分銅の数を入力
count = int(input())

# 分銅の重さを入力
# 後々の作業のため、昇順にソートしておく
weight = sorted([int(e) for e in input().split()], reverse=True)
sum_weight = sum(weight)

# 総重量の半分に等しくなった時点で最小であると判断できる
# ペアの単位として１以上、分銅の数未満で考える
for unit in range(1, count):
  for pair in itertools.combinations(weight, unit):
    if sum(pair) == sum_weight / 2:
      print(0)
      sys.exit()

# 等しく2等分できなかった場合
# 大きいものから順番に左右に振り分けていく
left = 0
right = 0

for element in weight:
  if left <= right:
    left += element
  else:
    right += element

print(abs(left - right))
"""

# 二重配列における重複を削除する関数
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


# 分銅の数を入力
count = int(input())

# 分銅の重さを入力
weight = [int(e) for e in input().split()]


# 左のお皿に乗せる個数のパターン数
# コメントを消して全体の分銅の数が偶数or奇数で場合分けすれば
# 偶数の時，for文の試行回数を少なくできるかも
combination_pattern = len(weight) // 2

# 重複する要素は削除した場合の分銅の重さリスト
weight_primaly = list(set(weight))
print(weight_primaly)

# 2つ以上の組み合わせの時を考える
# for i in range(2, combination_pattern + 1):
# print(weight_primaly)



# weightリストについてn個のとり方を考える
p = itertools.combinations(weight, 2)
# p = itertools.permutations(weight, 2)

left_pattern = []
right_pattern = []
for v in p:
  # タイプをtupleからリストにキャスト
  v = list(v)
  left_pattern.append(v)
  # print(type(v))
  # print(type(weight))

  # right_pattern.append(the_other_list)
  # print(v)

# print(pattern)
print(get_unique_list(left_pattern))

for row in get_unique_list(left_pattern):
  the_other_list = weight
  for element in row:
    the_other_list.remove(element)
  
  right_pattern.append(the_other_list)

print(get_unique_list(right_pattern))

left = 0
right = 0

