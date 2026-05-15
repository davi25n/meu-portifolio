#include <stdio.h>
#include <string.h>

int main(void) {
    int total;
    printf("Quantas palavras você deseja inserir? ");
    scanf("%d", &total);
    char palavras[total][100];  // Array de strings, cada uma com até 99 chars
    for (int i = 0; i < total; i++) {
        printf("Digite a palavra %d: ", i + 1);
        scanf("%s", palavras[i]);
    }
    for (int j = 0; j < total; j++) {
        printf("%s ", palavras[j]);
    }
    return 0;
}