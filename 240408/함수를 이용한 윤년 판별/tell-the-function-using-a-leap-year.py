year = int(input())

def judge_year(n):
    if n%100==0 and n%400!=0:
        return False
    if n%4==0:
        return True
   
    return False


if judge_year(year):
    print('true')
else:
    print('false')