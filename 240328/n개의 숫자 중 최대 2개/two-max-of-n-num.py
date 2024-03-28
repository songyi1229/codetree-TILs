# n = int(input())
# arr = list(map(int, input().split()))
# max_value = max(arr)
# diff_min  = max_value - arr[0]

# for i in arr:
#     if diff_min > max_value - i:
#         diff_min = max_value - i
#         se_max = i

# print(f"{max_value} {se_max}")

n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)

for i in arr:
    if max_value in arr:
        idx = arr.index(max_value)

new_arr = arr[0:idx]+arr[idx+1:]
se_max = max(new_arr)

print(f"{max_value} {se_max}")