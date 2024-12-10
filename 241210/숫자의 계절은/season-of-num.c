#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.

    int month;
    scanf("%d", &month);

    if (month==12 || month <= 2){
        printf("Winter");
    }
    else if (month >= 9){
        printf("Fall");
    }
    else if (month >= 6){
        printf("Summer");
    }
    else
        printf("Spring");

    return 0;
}