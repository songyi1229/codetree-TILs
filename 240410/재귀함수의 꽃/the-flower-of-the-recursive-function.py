n = int(input())

def nums(n):
    if n == 0:
        return
    print(n, end=" ")
    nums(n-1)
    print(n, end=" ")


nums(n)