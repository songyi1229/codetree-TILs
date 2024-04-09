word = input()

def judge(word):
    cnt = 0
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] != word[j]:
                cnt += 1
    return cnt


if judge(word) >= 2:
    print('Yes')
else:
    print('No')