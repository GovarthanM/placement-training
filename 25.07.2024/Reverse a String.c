#include <stdio.h>
#include <string.h>

int main() {
    char str[100], rev[100];
    printf("Enter string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        rev[i] = str[len - 1 - i];
    }
    rev[len] = '\0';
    printf("Reversed string: %s\n", rev);
    return 0;
}
