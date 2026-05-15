#include <stdio.h>
#include <string.h>

int main() {
    char palavra[100];
    char palavracode[100];
    printf("Digite uma palavra: ");
    scanf("%s", palavra);
    for (int i = 0, n = strlen(palavra); i < n; i++) {
        palavracode[i] = palavra[i] + 1; // Converte para o próximo caractere para scriptar
    }
    printf("Palavra codificada: %s", palavracode);
}