n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))



# b가 a의 연속부분수열인지 확인
def is_subsequence():
    for i in range(n1-n2+1):
        if is_same(i):
            return True
    return False

def is_same(n):
    for i in range(n2):
        if a[i+n] == b[i]:
            return False
    return True