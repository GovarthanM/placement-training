#include <stdio.h>

int main() {
    int n, i;
    unsigned long long factorial = 1;
    printf("Enter a number: ");
    scanf("%d", &n);
    if (n < 0)
        printf("Error\n");
    else {
        for(i = 1; i <= n; ++i) {
            factorial *= i;
        }
        printf("%llu\n",factorial);
    }
    return 0;
}
