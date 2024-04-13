a,b,c,d = list(map(int, input().split()))
ela_time = 0

while True:
    if a==c and b==d:
        break
    
    ela_time += 1
    b += 1

    if b==60:
        a += 1
        b = 0

print(ela_time)