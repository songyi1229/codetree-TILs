n = int(input())

def star(n):
    if n==0:
        return
    
    print("* "*n, end=" ")
    print()
    star(n-1)
    print("* "*n, end=" ")
    print()

star(n)