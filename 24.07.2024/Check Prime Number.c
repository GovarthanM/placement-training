#include <stdio.h>

int main() {
    int n, i, flag = 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    for(i = 2; i <= n/2; ++i) {
        if (n % i == 0) {
            flag = 1;
            break;
        }
    }
    if (n == 1) 
        printf("neither prime nor composite.\n");
    else {
        if (flag == 0)
            printf("prime");
        else
            printf("not a prime");
    }
    return 0;
}
