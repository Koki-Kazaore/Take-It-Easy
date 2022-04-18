line=input().split()
num1=int(line[0])
num2=int(line[1])
uma1=[]
uma2=[]
uma3=[]
for i in range(num1):
    rank1=int(input())
    uma1.append(rank1)
uma_1=0
for i in range(num1+1-num2):
    umA_1=uma1[i]+uma1[i+1]+uma1[i+2]
    umA_1=umA_1/(num2)
    if uma_1<umA_1:
        uma_1=umA_1

for i in range(num1):
    rank2=int(input())
    uma2.append(rank2)
uma_2=0
for i in range(num1+1-num2):
    umA_2=uma2[i]+uma2[i+1]+uma2[i+2]
    umA_2=umA_2/(num2)
    if uma_2<umA_2:
        uma_2=umA_2

for i in range(num1):
    rank3=int(input())
    uma3.append(rank3)
uma_3=0
for i in range(num1+1-num2):
    umA_3=uma3[i]+uma3[i+1]+uma3[i+2]
    umA_3=umA_3/(num2)
    if uma_3<umA_3:
        uma_3=umA_3

if uma_1<uma_2 and uma_1<uma_3:
    print("1")
elif uma_2<uma_1 and uma_2<uma_3:
    print("2")
else:
    print("3")