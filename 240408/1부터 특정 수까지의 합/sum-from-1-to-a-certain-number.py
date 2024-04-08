def print_sum(n):
    sum_val = 0
    for i in range(1, n+1):
        sum_val += i
        
    result = sum_val // 10
    return result







n_num = int(input())
result = print_sum(n_num)
print(result)