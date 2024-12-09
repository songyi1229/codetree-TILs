#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.

    int a_m, a_e, b_m, b_e;

    scanf("%d %d", &a_m, &a_e);
    scanf("%d %d", &b_m, &b_e);

    if (a_m > b_m && a_e>b_e) {
        printf("1");
    }
    else
        printf("0");

    return 0;
}


