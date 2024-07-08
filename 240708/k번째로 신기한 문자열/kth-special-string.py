# 어떠한 조건을 만족해야하는지 결정
# 1) 문자열 s의 길이가 문자열 t의 길이보다 짧음 안됨
# 2) 문자열 s에 대해 앞에서부터 문자열 t의 길이만큼의 문자가 정확히 t와 일치

n, k, t = tuple(input().split())
n, k = int(n), int(k)

# a가 b로 시작하는지 확인 함수
def starts_with(a,b):
    # b의 길이는 더 길면 안됨
    if len(a) < len(b):
        return False
    
    # b의 길이만큼 살펴보며, a와 문자열이 완벽히 동일한지 확인
    return a[:len(b)] == b


words = []
for _ in range(n):
    word = input()
    if starts_with(word, t):
        words.append(word)

words.sort()

print(words[k-1])