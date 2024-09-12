arr_str = input().split()

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

for i in range(0, 4):
    for j in range(1, 5):
        for k in range(2, 6):
            ans = get_diff(i,j,k)

            if ans < min_val:
                min_val = ans

print(min_val)