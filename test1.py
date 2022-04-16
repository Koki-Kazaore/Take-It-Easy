# Python 3.9.2

from numpy import average


setting = [int(e) for e in input().split()]
race = setting[0]
combination = setting[1]

horseA = []
horseB = []
horseC = []

for i in range(race):
  horseA.append(int(input()))
  
for i in range(race):
  horseB.append(int(input()))

for i in range(race):
  horseC.append(int(input()))

rankA = 18
rankB = 18
rankC = 18

for j in range(0, len(horseA) - combination + 1):
  ave = average(horseA[j:combination + j])
  if (ave < rankA):
    rankA = ave
# print("rankA:", rankA)

for j in range(0, len(horseB) - combination + 1):
  ave = average(horseB[j:combination + j])
  if (ave < rankB):
    rankB = ave
# print("rankB:", rankB)

for j in range(0, len(horseC) - combination + 1):
  ave = average(horseC[j:combination + j])
  if (ave < rankC):
    rankC = ave
# print("rankC:", rankC)

if (rankA < rankB and rankA < rankC):
  print(1)

elif (rankB < rankA and rankB < rankC):
  print(2)

else:
  print(3)