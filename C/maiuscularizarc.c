#include <stdio.h>
#include <string.h>

int main(void) {
    char palavra[100];
    printf("Digite uma palavra minuscula: ");
    scanf("%s", palavra);
    for (int i = 0, n = strlen(palavra); i < n; i++) {
        if (palavra[i] >= 'a' && palavra[i] <= 'z') {
            palavra[i] = palavra[i] - 32; // Converte para maiúscula
            printf("%c", palavra[i]);
        }
        else {
            printf("%c", palavra[i]); // Imprime o caractere sem alteração
        }
    }
    printf("\n");
    return 0;
}