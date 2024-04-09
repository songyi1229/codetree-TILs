a, b = tuple(map(int, input().split()))

def judge(a,b):
    if a>b:
        a*=2
        b+=10
    else:
        a+=10
        b*=2

    return a,b


a,b = judge(a,b)
print(a,b, end=" ")