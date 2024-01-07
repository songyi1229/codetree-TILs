a, b = map(int, input().split())  #변수 선언 및 입력

print(f"{a//b}.",end="")   #정수 부분 출력 
a %= b   #a를 b로 나눈 후 나머지를 a에 할당

for _ in range(20):  #소수점 20째자리 하나씩 계산
    print((a*10)//b, end="")   #나머지에 10을 곱한 값을 b로 나눈 몫 출력
    a = (a*10) % b   #a를 b로 나눈 후 나머지 갱신