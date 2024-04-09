y, m, d = map(int, input().split())


def yoon_year(y):
    if y%4 ==0 and y%100==0 and y%400==0:
        return True
    if y%4==0 and y%100==0:
        return False
    if y%4 ==0:
        return True
    return False

def month_day(m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        return 28     


def date_exist(y,m,d):
    if yoon_year(y):
        if m==2:
            if d<=29:
                return True
        if d <= month_day(m):
            return True
    
    else:
        if d <= month_day(m):
            return True
    
        return False


if date_exist(y,m,d):
    if m in [3,4,5]:
        print('Spring')
    elif m in [6,7,8]:
        print('Summer')
    elif m in [9,10,11]:
        print('Fall')
    elif m in [1,2,12]:
        print('Winter')
else:
    print(-1)