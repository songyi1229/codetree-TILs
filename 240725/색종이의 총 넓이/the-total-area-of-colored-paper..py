offset = 100
max_v = 200

n = int(input())

two_dim = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


checked = [
    [0] * (max_v + 1)
    for _ in range(max_v + 1)
]

for x1, y1 in two_dim:
    x1, y1 = x1 + offset, y1 + offset

    for x in range(x1, x1 + 8):
        for y in range(y1, y1 + 8):
            checked[x][y] = 1


area = 0





for x in range(0, max_v + 1):
    for y in range(0, max_v + 1):
        if checked[x][y] == 1:
            area += 1


print(area)