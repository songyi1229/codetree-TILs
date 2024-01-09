a,b = map(int, input().split())
sum_val = 0
cnt = 0

for i in range(a, b+1):
    if i%5 == 0 or i%7 == 0:
        sum_val += i
        cnt += 1

mean = sum_val/cnt

print(sum_val, end =" ")
print(f"{mean:0.1f}")