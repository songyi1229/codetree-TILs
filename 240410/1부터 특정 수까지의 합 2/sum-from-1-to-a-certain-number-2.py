n = int(input())
hap = 0

def cal_sum(n):
    global hap
    if n==0:
        return
    hap += n
    cal_sum(n-1)
    return hap
      



print(cal_sum(n))