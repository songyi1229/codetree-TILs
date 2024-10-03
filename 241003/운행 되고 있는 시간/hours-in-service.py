n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def find_time(a, b, c, d):
    check = []
    for i in range(a, b):
        if i not in check:
            check.append(i)
    for ii in range(c, d):
        if ii not in check:
            check.append(ii)
    
    time = len(check)
    
    return time


ans = 0

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]

        time = find_time(x1, y1, x2, y2)

        ans = max(ans, time)

print(ans)