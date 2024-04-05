n, m = tuple(map(int, input().split()))

max_val = 0

for i in range(1,100):
    if n%i==0 and m%i==0:
        max_val = i
    
print(max_val)