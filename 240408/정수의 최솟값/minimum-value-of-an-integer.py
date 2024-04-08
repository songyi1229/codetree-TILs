def find_min(a,b,c):
    return min(a,b,c)





a_num, b_num, c_num = map(int, input().split())
result = find_min(a_num, b_num, c_num)
print(result)