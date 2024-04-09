arr1 = input()
arr2 = input()
n1 = len(arr1)
n2 = len(arr2)


def is_same(n):
    for i in range(n2):
        if arr1[n+i] != arr2[i]:
            return False
    return True


def is_seq():
    
    for i in range(n1-n2+1):
        if is_same(i):
            return i
    return -1


print(is_seq())