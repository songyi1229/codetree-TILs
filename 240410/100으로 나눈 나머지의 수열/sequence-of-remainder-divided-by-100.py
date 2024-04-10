n = int(input())

def seq(n):
    if n==1:
        return 2
    if n==2:
        return 4
    if n==0:
        return 0
    if n>20:
        return 0

    return (seq(n-1)*seq(n-2))%100

print(seq(n))