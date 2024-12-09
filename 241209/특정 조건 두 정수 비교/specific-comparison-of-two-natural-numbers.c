#include <stdio.h>

int main() {
    // 여기에 코드를 작성해주세요.

    int a, b;
    int same, small;

    scanf("%d %d", &a,&b);

    small = a<b ? 1:0;
    same = a==b ? 1:0;
    printf("%d %d", small, same);
    return 0;
}