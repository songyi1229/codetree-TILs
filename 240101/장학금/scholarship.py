j, g = input().split()
j = int(j)
g = int(g)

if j>=90:
    if g>=95:
        print(100000)
    elif g>=90:
        print(50000)
    else:
        print(0)
else:
    print(0)