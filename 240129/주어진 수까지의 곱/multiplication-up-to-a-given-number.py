a,b = map(int, input().split())

prod = 1

if a>b:
    for i in range(b, a+1):
        prod *= i
else:
    for i in range(a, b+1):
        prod *= i

print(prod)