arr = list(map(int, input().split()))



for i in arr:
    if i == 0:
        k=i
        break

print(arr[k-1]+arr[k-2]+arr[k-3])