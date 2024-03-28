n = int(input())
arr = list(map(int, input().split()))

min_n = min(arr)
cnt = 0

for i in arr:
    if i == min_n:
        cnt += 1

print(f"{min_n} {cnt}")