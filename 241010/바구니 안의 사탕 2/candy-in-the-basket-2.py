n, k = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


max_cnt = 0
store = [0]*101

for candy, place in arr:
    store[place] = candy

for i in range(len(store) - (2*k + 1) + 1):
    cnt = 0
    for j in range(i, i+2*k + 1):
        cnt += store[j]
    max_cnt = max(max_cnt, cnt)


print(max_cnt)