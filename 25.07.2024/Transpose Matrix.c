#include <stdio.h>

int main() {
    int m, n;
    printf("Enter rows and columns : ");
    scanf("%d %d", &m, &n);
    int matrix[m][n], t[n][m];
    printf("Enter elements :\n");
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            scanf("%d", &matrix[i][j]);
        }
    }
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            t[j][i] = matrix[i][j];
        }
    }
    printf("Transpose :\n");
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            printf("%d ", t[i][j]);
        }
        printf("\n");
    }
    return 0;
}
