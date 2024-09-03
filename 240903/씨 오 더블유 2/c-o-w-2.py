n = int(input())
arr = input()
leng = len(arr)

cnt = 0

for i in range(leng):
    for j in range(i+1, leng):
        for k in range(j+1, leng):
            if arr[i]=='C' and arr[j]=='O' and arr[k]=='W':
                cnt += 1

print(cnt)