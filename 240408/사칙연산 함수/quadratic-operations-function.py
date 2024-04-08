a,o,c = input().split()
a = int(a)
c = int(c)

def plus(a,c):
    return a+c

def mul(a,c):
    return a*c

def sub(a,c):
    return a-c

def div(a,c):
    return int(a/c)

if o == '+':
    print(f"{a} {o} {c} = {plus(a,c)}")
elif o == '-':
    print(f"{a} {o} {c} = {sub(a,c)}")
elif o == '/':
    print(f"{a} {o} {c} = {div(a,c)}")
elif o == '*':
    print(f"{a} {o} {c} = {mul(a,c)}")     
else:
    print('False')