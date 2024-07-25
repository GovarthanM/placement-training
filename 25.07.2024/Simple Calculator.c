#include <stdio.h>

int main() {
    char op;
    float num1, num2, result;
    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &op);
    printf("Enter two Numbers: ");
    scanf("%f %f", &num1, &num2);
    switch(op) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '*': result = num1 * num2; break;
        case '/': result = num1 / num2; break;
        default: printf("Error! Operator is not correct\n"); return 1;
    }
    printf("%.2f\n", result);
    return 0;
}
