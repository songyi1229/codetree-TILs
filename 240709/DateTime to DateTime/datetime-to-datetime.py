a, b, c = tuple(input().split())
a, b, c = int(a), int(b), int(c)

def daytomin(day):
    return (day - 11) * 24 * 60

def timetomin(h, m):

    return (h*60 + m)-(11*60+11)


print(daytomin(a) + timetomin(b, c))