ma, ea = input().split()
mb, eb = input().split()
ma = int(ma)
ea = int(ea)
mb = int(mb)
eb = int(eb)

if ma > mb:
    print("A")
elif ma<mb:
    print("B")

elif ma == mb:
    if ea>eb:
        print("A")
    else:
        print("B")