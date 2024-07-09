a, b, c = tuple(input().split())
a, b, c = int(a), int(b), int(c)

def daytomin(day):
    return (day - 11) * 24 * 60

def timetomin(h, m):

    return (h*60 + m)-(11*60+11)

if a<11 or (a<=11 and b<11) or (a<=11 or b<=11 or c<11):
    print("-1")
else:
    print(daytomin(a) + timetomin(b, c))