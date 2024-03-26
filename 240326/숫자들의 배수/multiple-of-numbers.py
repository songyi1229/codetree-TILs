n=int(input())

arr = []
cnt = 0

arr.append(n)

for i in range(2, 11):
    a = n*i
    arr.append(n*i)


for j in arr:
    print(j, end=" ")
    if j%5==0:
        cnt+=1
    if cnt >= 2:
        break