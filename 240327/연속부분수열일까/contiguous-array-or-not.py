a, b = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = [0]*(len(B)+1)  # A의 인덱스 저장

for i in range(len(B)):
    if B[i] in A:
        idx = A.index(B[i])
        cnt[i]=idx + 1
    else:
        continue

# for j in range(len(cnt)):
#     if cnt[j+1] - cnt[j] == 1:
#         print('No')
#     else:
#         print('Yes')
if cnt[1] - cnt[0] == 1:
    print('Yes')
else:
    print('No')