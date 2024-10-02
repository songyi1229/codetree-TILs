n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
# 세자리 수 만들기
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
           
            if i==j or j==k or i==k:  # 세자리 수는 서로 다름
                continue

            suc = True

            for a, num_cnt1, num_cnt2 in arr:
                # 백:x, 십:y, 일:z
                x = a//100
                y = a//10%10
                z = a%10
                cnt1=0
                cnt2=0

                if i == x:
                    cnt1+=1
                if j == y:
                    cnt1+=1
                if k == z:
                    cnt1+=1
                if i == y or i == z:
                    cnt2+=1
                if j == x or j == z:
                    cnt2+=1
                if k == x or k == y:
                    cnt2+=1  

                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    suc = False
                
            if suc:
                cnt += 1

print(cnt)