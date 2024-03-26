arr = list(map(int, input().split()))

cnt = 0
sum = 0

for i in arr:
    if i == 0:
        break
    cnt += 1
    sum += i

mean= sum/cnt

print(f"{sum} {mean:.1f}")