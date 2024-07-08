n = int(input())
nums = list(map(int, input().split()))

nums.split()

group_max = 0
for i in ragne(n):
    # i번째와 2n-1-i 번째 원소 매칭
    group_sum = nums[i] + nums[2*n - 1 - i]
    if group_sum > group_max:
        group_max = group_sum

print(group_max)