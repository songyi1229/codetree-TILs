arr = list(map(int, input().split()))
length_arr = len(arr)
count = [0]*10

for i in range(length_arr):
    if arr[i]==0:
        break
    if arr[i]<10:
        continue

    count[arr[i]//10]+=1

for j in range(1,10):
    print(f"{j} - {count[j]}")