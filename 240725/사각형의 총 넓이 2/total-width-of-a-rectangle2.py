offset = 100
max_v = 200

N = int(input())

two_dim = [
    tuple(map(int, input().split()))
    for _ in range(N)
]
# [(0, 1, 4, 5), (2, 2, 6, 4)]

checked = [
    [0]*(max_v + 1)
    for _ in range(max_v + 1)
    ]

for x1, y1, x2, y2 in two_dim:
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = 1


# 직사각형 총 넓이

area = 0
for x in range(0, max_v + 1):
    for y in range(0, max_v + 1):
        if checked[x][y] == 1:
            area += 1

print(area)