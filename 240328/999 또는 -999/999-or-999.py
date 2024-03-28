n = list(map(int, input().split()))
arr = []
for i in range(100):
    if n[i] == 999 or n[i] == -999:
        break
    arr.append(n[i])

max_n = max(arr)
min_n = min(arr)

print(f"{max_n} {min_n}")