#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
   
    char palavra[argc - 1][100];
    char palavracode[argc - 1][100];
    if (argc >= 2) {
        printf("ola ");
        for (int i = 0; i < argc - 1; i++) {
            strcpy(palavra[i], argv[i + 1]);
            for (int j = 0, n = strlen(palavra[i]); j < n; j++) {
                palavracode[i][j] = palavra[i][j] + 1; // Converte para o próximo caractere para scriptar   
            }
            printf("%s ", palavracode[i]);
        }   
    }
    else {
        printf("ola mundo\n");
    }

    return 0;
}