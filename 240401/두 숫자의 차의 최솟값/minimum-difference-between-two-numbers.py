n = int(input())
arr = list(map(int, input().split()))

min_diff = arr[1] - arr[0]

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        diff = arr[j] - arr[i]
        if abs(diff) < min_diff:
            min_diff = diff

print(min_diff)