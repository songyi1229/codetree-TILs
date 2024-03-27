# 감기 증상 있 Y
# 감기 증상 없 N

# Y & 37이상 -> A
# N & 37이상 -> B
# Y & 37 이하 -> C
# N & 37 이하 -> D

# 한번에 3명씩 검사
# 만약 A로 가는 사람 2명 이상 -> E

count = [0]*4

for i in range(3):  
    a,b=list(input().split())
    b= int(b)

    if a=='Y' and int(b)>=37:
        count[0]+=1
    
    elif a=='N' and int(b)>=37:
        count[1]+=1
    elif a=='Y' and int(b)<37:
        count[2]+=1
    elif a=='N' and int(b)<37:
        count[3]+=1        

  
for j in count:
    print(j, end=" ")   
if count[0]>=2:
    print('E')