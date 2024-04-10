def f(n):
    if n==1:
        return 2
    if n==2:
        return 7

    return f(n-1)+2*f(n-2)