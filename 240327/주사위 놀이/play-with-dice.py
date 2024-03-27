count = [0]*7
arr = list(map(int, input().split()))

for i in arr:
    count[i]+=1

for j in range(1,7):
    cnt = count[j]
    print(f"{j} - {cnt}")