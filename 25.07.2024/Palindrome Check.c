#include <stdio.h>

int main() {
    int n, re = 0, remainder, o;
    printf("Enter an integer: ");
    scanf("%d", &n);
    o = n;
    while (n != 0) {
        remainder = n % 10;
        re = re * 10 + remainder;
        n /= 10;
    }
    if (o == re)
        printf("%d is a palindrome.\n", o);
    else
        printf("%d is not a palindrome.\n", o);
    return 0;
}
