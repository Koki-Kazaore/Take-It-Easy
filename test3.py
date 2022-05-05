import sys

# 入力
INPUT = input().split()
purchase = int(INPUT[0])
kinds = int(INPUT[1])
result = []
# 種類別で出てきた数をカウントするリスト
# 例(4種類の場合) count = [0, 0, 0, 0]
card_count = [0] * kinds

# 入力
for i in range(purchase):
  result.append(int(input()))

# print(result)

# 何回目で全種類そろったかをカウントする変数
search_count = 1

# 上で入力したresultリストから1つずつ取り出し、
# その値によってcountリストをインクリメント
for j in result:
  card_count[j - 1] += 1
  # countリストに0がなくなったらすべての種類が出たと判断
  if 0 not in card_count:
    print(search_count)
    # やるべきことが終わったため、強制終了
    sys.exit()
  
  search_count += 1

# for文で強制終了されなかったということは全ての種類見つからなかったと判断
print("unlucky")