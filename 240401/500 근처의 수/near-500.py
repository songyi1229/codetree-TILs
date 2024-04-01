arr = list(map(int, input().split()))

bigger_500 = list()
smaller_500 = list()

for i in arr:
    if i < 500:
        smaller_500.append(i)
    elif i > 500:
        bigger_500.append(i)
    else: 
        continue

print(max(smaller_500), min(bigger_500))