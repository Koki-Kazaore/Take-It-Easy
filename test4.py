# 入力
quantities = int(input())

shopping = {}
points = 0
food = 0
book = 0
cloth = 0
other = 0

for i in range(quantities):
  kinds, price = map(int, input().split())
  shopping.update({kinds: price})

  if kinds == 0:
    food += price

  elif kinds == 1:
    book += price

  elif kinds == 2:
    cloth += price

  else:
    other += price

points += (food // 100) * 5
points += (book // 100) * 3
points += (cloth // 100) * 2
points += (other // 100) * 1
  
print(points)