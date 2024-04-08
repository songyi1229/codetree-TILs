a,b = tuple(map(int, input().split()))

def judge_369(n):
    while n>0:
        if n%10==3 or n%10==6 or n%10==9:
            return True
        
        n//=10
    return False

def game(n):
    return n%3==0 or judge_369(n)

cnt = 0
for i in range(a, b+1):
    if game(i):
        cnt+=1
print(cnt)