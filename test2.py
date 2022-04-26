import re

count = int(input())

users = {}


for i in range(count):
  temp = input()
  id = int(re.sub(r"\D", "", temp))
  users.update({id: temp})

users_sorted = sorted(users.items(), key=lambda x:x[0])
# print(users_sorted)

for myvalue in users_sorted:
    print(myvalue[1])