a, b= tuple(map(int, input().split()))

def prime(n):
    if n == 1:
        return False

    for j in range(2, n):
        if n%j==0:
            return False
    return True

def jud_even(n):
    if n == 1 or n==100:
        return False
    if (n//10 + n%10) % 2==0:
        return True


cnt = 0
for i in range(a, b+1):
    if prime(i) and jud_even(i):
        cnt += 1
print(cnt)