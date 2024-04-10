import math
n = int(input())
arr = list(map(int, input().split()))
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        first = arr[0]
        rest_lcm = lcm_array(arr[1:])
        return lcm(first, rest_lcm)

print(lcm_array(arr))