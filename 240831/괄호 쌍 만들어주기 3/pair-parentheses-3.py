arr = input()
leng = len(arr)

cnt = 0 
for i in range(leng):
    for j in range(i+1, leng):

        if arr[i] == '(' and arr[j] == ')':

            cnt += 1
            
print(cnt)