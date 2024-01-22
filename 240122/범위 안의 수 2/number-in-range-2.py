sum = 0
cnt = 0
for i in range(1, 11):
    n = int(input())

    if n >=0 and n<=200:
        sum += n
        cnt += 1
        

mean = sum / cnt

print(sum, end=" ")
print(f"{mean:0.1f}")