arr = list(map(int, input().split()))

sum = 0

cnt =0

for i in arr:
    if i>= 250:
        break

    sum += i
    cnt = cnt + 1



mean = sum/cnt

print(f"{sum} {mean:0.1f}")