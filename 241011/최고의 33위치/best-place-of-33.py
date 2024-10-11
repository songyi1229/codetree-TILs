n = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_num_gold(x_s, y_s, x_e, y_e):
    num_gold = 0

    for x in range(x_s, x_e+1):
        for y in range(y_s, y_e+1):
            num_gold += a[x][y]

    return num_gold

max_num = 0
for i in range(n):
    for j in range(n):
        if i+2>=n or j+2>=n:
            continue
        num_gold = get_num_gold(i, j, i+2, j+2)

        max_num = max(max_num, num_gold)

print(max_num)