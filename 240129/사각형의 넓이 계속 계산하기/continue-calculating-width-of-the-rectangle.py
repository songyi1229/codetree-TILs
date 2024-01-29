while True:
    n = input().split()
    g = int(n[0]) 
    s = int(n[1])
    m = n[2]

    print(g*s)

    if m == 'C':
        break