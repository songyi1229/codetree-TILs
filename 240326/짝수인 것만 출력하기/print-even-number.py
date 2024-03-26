n = int(input())
arr = list(map(int, input().split()))

new_arr = [i for i in arr if i%2==0]
for j in new_arr:
    print(j, end=" ")