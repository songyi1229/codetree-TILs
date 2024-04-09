a,b = tuple(map(int, input().split()))



def change_value(a,b):

    if a>b:
        a+=25
        b*=2
    else:
        b+=25
        a*=2

    print(a, b, end=" ")


change_value(a,b)