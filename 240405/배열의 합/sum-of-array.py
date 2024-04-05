arr = [
    list(map(int, input().split()))
    for _ in range(4)
]
sum_val = 0
for i in range(4):
    sum_val = sum(arr[i])
    print(sum_val)