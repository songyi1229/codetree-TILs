arr = input()
leng = len(arr)

cnt = 0
for i in range(leng):
    for j in range(i+1, leng-1):
        if arr[i]=='(' and arr[i+1]=='(' and arr[j]==')' and arr[j+1]==')':
            cnt += 1

print(cnt)