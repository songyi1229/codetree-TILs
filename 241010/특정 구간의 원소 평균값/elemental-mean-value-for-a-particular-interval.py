n = int(input())
arr = list(map(int, input().split()))


cnt = 0

for i in range(n):
    for j in range(i, n):
        store = []
        for k in range(i, j+1):
            
            store.append(arr[k])
            
        mean = sum(store) / len(store)
        
        if mean in store:
            cnt += 1

print(cnt)