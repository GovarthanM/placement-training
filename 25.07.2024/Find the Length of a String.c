#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("Enter string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';
    printf("Length : %lu\n", strlen(str));
    return 0;
}
