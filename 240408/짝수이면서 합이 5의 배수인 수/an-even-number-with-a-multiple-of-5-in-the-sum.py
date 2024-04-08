def is_even(N):
    return N%2==0 and (N//10 + N%10)%5==0


n = int(input())
if is_even(n):
    print('Yes')
else:
    print('No')