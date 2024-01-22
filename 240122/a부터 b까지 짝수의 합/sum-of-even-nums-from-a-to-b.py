a,b = map(int, input().split())
sum = 0
if b>=a:
    for i in range(a, b+1):
        if i%2==0:
            sum += i
else:
    for i in range(b, a+1):
        if i%2==0:
            sum += i

print(sum)