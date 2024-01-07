a,b=map(int, input().split())
for i in range(a, b+1):
    if i%2==0 and i<=b:
        i+=3
        print(i, end=" ")
        
    elif i%2!=0 and i<=b:
        i*=2
        print(i, end=" ")