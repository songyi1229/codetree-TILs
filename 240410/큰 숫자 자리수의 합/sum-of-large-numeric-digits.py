a,b,c = map(int, input().split())
n = a*b*c

def sum_val(n):
    if n == 0:
        return 0

    return sum_val(n//10) + n%10

print(sum_val(n))