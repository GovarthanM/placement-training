#include <stdio.h>

int main() {
    int n, r = 0, remainder;
    printf("Enter an Numbers: ");
    scanf("%d", &n);
    while (n != 0) {
        remainder = n % 10;
        r = r * 10 + remainder;
        n /= 10;
    }
    printf("Reversed Number: %d\n", r);
    return 0;
}
