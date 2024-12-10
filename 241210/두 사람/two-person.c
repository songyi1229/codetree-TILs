#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.

    int a_age, b_age;
    char a_s, b_s;
    scanf("%d %c\n%d %c", &a_age, &a_s, &b_age, &b_s);

    if ((a_age >=19 && a_s == 'M') || (b_age >=19 && b_s == 'M')){
        printf("1");
    }
    else
        printf("0");


    return 0;
}