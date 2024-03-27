# 1. n 원소 개수 q 질문 개수
# 2. n개만큼 숫자 입력 받음 
# 3. q개만큼 질문을 받는데 q번 반복해서 차레차례 입력 받으면서 출력해도 됨

# 3 3
# 1 8 5   숫자 입력 받음
# 1 1     질문 1번
# 2 5     질문 2번
# 3 1 2   질분 3번


n, q = map(int, input().split())
nums = list(map(int, input().split()))
idx = -1
for i in range(q):
    ques = list(map(int, input().split()))
    if ques[0]==1:
        f = ques[1]-1
        print(nums[f])

    elif ques[0]==2: 
        s = ques[1]
        for k, val in enumerate(nums):
            if val == s:
                idx = k
                break
                     

        if idx == -1:
            print(0)  
        else:
            print(idx+1) 

    elif ques[0]==3:  

        tt = ques[1]
        ttt = ques[2]
        for j in range(tt-1, ttt):
            print(nums[j], end=" ")
        print(end="\n")