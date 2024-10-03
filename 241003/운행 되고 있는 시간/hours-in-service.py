n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def find_time(a, b):
    for i in range(a, b):
        if i not in check:
            check.append(i)
    
    return len(check)


ans = 0

for i in range(n):
    check=[]
    for j in range(n):
        if j==i:
            continue
        x1, y1 = arr[j]

        time = find_time(x1, y1)
    ans = max(ans, time)

print(ans)