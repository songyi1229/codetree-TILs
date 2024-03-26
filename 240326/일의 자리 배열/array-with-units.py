arr = list(map(int, input().split()))

for i in range(3, 11):
    sum = arr[-1] + arr[-2]
    aa = sum%10
    arr.append(aa)

for j in arr:
    print(j, end=" ")