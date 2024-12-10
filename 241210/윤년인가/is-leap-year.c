#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.

    int y;
    scanf("%d", &y);

    if (y%100==100 || y%100!=0) {
        printf("false");
    }
    else if (y%4!=0){
        printf("true");
    }
    else
        printf("false");

    return 0;
}


// 윤년 판단
// 1. 4로 나누어 떨어짐
// 2. 100으로 나누어 떨어짐 동시에 400으로는 나누어 떨어지지 않는 해는 평년