a = list(input())
b = list(input())



def judge(a,b):
    if len(a) != len(b):
        return False
    for i,j in zip(a,b):
        if i==j:
            return True
    return False

a.sort()
b.sort()

if judge(a,b):
    print('Yes')
else:
    print('No')