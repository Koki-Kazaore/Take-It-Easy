# 入力
countries = int(input())

medals = [input().split() for i in range(countries)]

# リストの中身をint型に変換する
for i in range(len(medals)):
  for j in range(3):
    medals[i][j] = int(medals[i][j])

result = sorted(medals, reverse=True)

for a in result:
    print(*a)