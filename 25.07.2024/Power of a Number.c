#include <stdio.h>

int main() {
    int base, exp;
    long long result = 1;
    printf("base number: ");
    scanf("%d", &base);
    printf("exponent: ");
    scanf("%d", &exp);
    for (int i = 1; i <= exp; ++i) {
        result *= base;
    }
    printf("%d^%d = %lld\n", base, exp, result);
    return 0;
}
