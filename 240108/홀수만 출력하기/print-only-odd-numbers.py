n = int(input())
arr=[]
arr.append(n)
for i in range(n):
    num = int(input())
    arr.append(num)

for i in arr:
    if i%3==0 and i%2==1:
        print(i)