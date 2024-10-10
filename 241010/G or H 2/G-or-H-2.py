n = int(input())
arr = [
    input().split()
    for _ in range(n)
]

place = [0] * 101

# G면 2, H면 1
for a, b in arr:
    a = int(a)
    if b == 'G':
        place[a] = 2
    else:
        place[a] = 1


max_len = 0
for i in range(len(place)):
    for j in range(i+1, len(place)):
        if place[i] == 0 or place[j] == 0:
            continue
        
        cnt_g = 0
        cnt_h = 0
        
        for k in range(i, j+1):
            if place[k] == 2:
                cnt_g += 1
            if place[k] == 1:
                cnt_h += 1

        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            length = j-i
            max_len = max(max_len, length)

print(max_len)