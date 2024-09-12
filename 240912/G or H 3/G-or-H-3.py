MAX_NUM = 10000
n, k = tuple(map(int, input().split()))

placed = [0] * (MAX_NUM+1)

max_elem = 0
for _ in range(n):
    elem, point = input().split()
    elem = int(elem)

    if point == 'G':
        placed[elem] = 1
    else:
        placed[elem] = 2



ans = 0

for i in range(MAX_NUM - k + 1):
    max_score = 0
    for j in range(i, i+k+1):
        max_score += placed[j]
        ans = max(ans, max_score)


print(ans)