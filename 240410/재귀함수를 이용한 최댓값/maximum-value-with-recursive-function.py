n = int(input())
arr = list(map(int, input().split()))

def find_max(n):
    if n==0:
        return

    return max(arr)

print(find_max(n))