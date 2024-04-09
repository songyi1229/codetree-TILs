n = int(input())
arr = list(map(int, input().split()))


def judge_even(n):
    if n%2==0:
        return True
    else:
        return False

for i in arr:
    if judge_even(i):
        print(int(i/2), end=" ")
    else:
        print(i, end= " ")