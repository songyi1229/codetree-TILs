arr_str = input().split()
n = len(arr_str)
arr = []
for i in arr_str:
    i = int(i)
    arr.append(i)

def get_diff(a, b, c):
    team1 = arr[a] + arr[b] + arr[c]
    team2 = sum(arr) - team1
    return abs(team1 - team2)


min_val = 100
ans = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            ans = get_diff(i,j,k)

            if ans < min_val:
                min_val = ans

print(min_val)