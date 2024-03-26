arr = list(map(int, input().split()))


for i in range(10):
    if arr[i] == 0:
        arr.pop()
arr = arr[::-1]
for j in arr:
    print(j, end=" ")