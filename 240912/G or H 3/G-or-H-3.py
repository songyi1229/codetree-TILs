# for elem in arr:
#     placed[elem] = 1

n, k = tuple(map(int, input().split()))

placed = [0] * 101
arr = [0] * (n+1)

max_elem = 0
for _ in range(n):
    elem, point = input().split()
    elem = int(elem)
    arr.append(elem)
    if point == 'G':
        placed[elem] = 1
    else:
        placed[elem] = 2
    if elem > max_elem:
        max_elem = elem

arr.sort()

ans = 0

for i in arr:
    max_score = 0
    for j in range(i, i+k+1):
        max_score += placed[j]
        ans = max(ans, max_score)


print(ans)