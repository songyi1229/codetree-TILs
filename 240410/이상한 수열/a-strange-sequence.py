n = int(input())


def strange(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==0:
        return 0
    if n>15:
        return 0
    
    return strange(n//3)+strange(n-1)

print(strange(n))