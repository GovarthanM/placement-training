#include <stdio.h>

int main() {
    int n, i, f= 0;
    printf("Enter a number: ");
    scanf("%d", &n);
    for(i = 2; i <= n/2; ++i) {
        if (n % i == 0) {
            f = 1;
            break;
        }
    }
    if (n == 1) 
        printf("neither prime nor composite.\n");
    else {
        if (f == 0)
            printf("%d is a prime number.\n", n);
        else
            printf("%d is not a prime number.\n", n);
    }
    return 0;
}
