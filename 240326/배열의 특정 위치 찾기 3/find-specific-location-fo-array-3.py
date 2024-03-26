arr = list(map(int, input().split()))

sum_val = 0

for i in arr:
    sum_val += i
    if i == 0:
        break
print(sum_val)