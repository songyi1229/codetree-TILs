# c시 d분까지 몇 분 흘렀는지 계산 - a시 b분 몇분?

a,b,c,d = tuple(input().split())
a,b,c,d = int(a), int(b), int(c), int(d)

ab_min = a*60 + b
cd_min = c*60 + d

ela_min = cd_min - ab_min

print(ela_min)